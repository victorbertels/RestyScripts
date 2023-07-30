import requests
store_url = "https://www.ubereats.com/au/store/carls-jr-cranbourne/Ofg-GyyoSxqoEDU1hrnrbQ?diningMode=DELIVERY&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMjEtNSUyME1vbmFoYW5zJTIwUmQlMjIlMkMlMjJyZWZlcmVuY2UlMjIlM0ElMjJDaElKRFpjOUFFNE8xbW9SVzUxaWczRHJkZmMlMjIlMkMlMjJyZWZlcmVuY2VUeXBlJTIyJTNBJTIyZ29vZ2xlX3BsYWNlcyUyMiUyQyUyMmxhdGl0dWRlJTIyJTNBLTM4LjExMDI0OTMlMkMlMjJsb25naXR1ZGUlMjIlM0ExNDUuMjYzODglN0Q%3D&ps=1"
def get_uber_store_uuid(store_url: str) -> str:
    if not store_url:
        return ""
    response = requests.get(store_url)
    uuid = response.text.split("\\u0022stores\\u0022:{\\u0022")[1][:36]
    print(uuid)
    return uuid

    """
    except as error:
        print(f"Error occured during parsing uber store uuid: {error}")
        return ""
        """
get_uber_store_uuid(store_url)
