from collections import defaultdict
import time

cli = lcli


def upgradeLoc(locationId):
    location = cli.locations.get(locationId)
    if location.posSettings.kounta.useDefaultPLU:
        print(f"location {locationId} already have useDefaultPLU")
        return True
    upgradeResult = True
    # update settings
    cli.locations.update(locationId, {"posSettings.kounta.useDefaultPLU": True}, override=1, propagate='pos')
    # sync products
    print("start productSync preview")
    opReportResult = cli.call(f"/v2/locations/{locationId}/syncProducts?previewSync=true", method="POST")
    # check for errors and warnings
    opReport = cli.operationReports.get(opReportResult.get("_id"))
    while opReport.operationStatus != 90:
        opReport = cli.operationReports.get(opReportResult.get("_id"))
        print(f"wait success(90)  status for op report,  current status: {opReport.operationStatus}")
        time.sleep(10)
        if opReport.operationStatus == 120:
            print(opReport.status, location)
            upgradeResult = False
            break
    if errors := opReport.errors:
        print("errors for", locationId, errors)
        upgradeResult = False
    if warnings := opReport.warnings:
        print("warnings for", locationId, warnings)
    if upgradeResult:
        print("start force productSync")
        opReportResult = cli.call(f"/v2/locations/{locationId}/syncProducts?forceUpdate=true", method="POST")
        opReport = cli.operationReports.get(opReportResult.get("_id"))
        while opReport.operationStatus != 90:
            opReport = cli.operationReports.get(opReportResult.get("_id"))
            print(f"wait success(90)  status for op report,  current status: {opReport.operationStatus}")
            time.sleep(10)
            if opReport.operationStatus == 120:
                print(opReport.status, location)
                upgradeResult = False
                break
        if errors := opReport.errors:
            print("errors during product sync for", locationId, errors)
            upgradeResult = False
    if not upgradeResult:
        print(f"failed to sync product for {location.name}, revert useDefaultPLU")
        cli.locations.update(locationId, {"posSettings.kounta.useDefaultPLU": False}, override=1, propagate='pos')
    return upgradeResult


def upgradeAccount(accId, pushMenu: bool = False):
    accountMenus = cli.channelMenus.list_all(q={'account': accId})
    locations = cli.locations.list_all(q={"account": accId, 'posSettings.kounta.useDefaultPLU': {"$ne": True}})
    menusByLink = defaultdict(set)
    for menu in accountMenus:
        for link in menu.activeChannelLinkIds or []:
            menusByLink[link].add(menu._id)
    for l in locations:
        if l.posSettings.kounta.useDefaultPLU:
            print(f"location {l.name} already have useDefaultPLU")
            continue
        isFullyUpdated = upgradeLoc(l._id)
        if isFullyUpdated:
            for cl in l.channelLinks:
                clObject=cli.channelLinks.get(cl)
                if clObject.name == "Test channel":
                    continue
                if clMenu := menusByLink.get(cl):
                    data = {'account': accId, 'channelLinks': [cl], 'menus': list(clMenu),
                            'serverUrl': 'https://api.deliverect.com'}
                    print(data)
                    if pushMenu:
                        print(cli.call('/pushMenus', 'POST', json=data))