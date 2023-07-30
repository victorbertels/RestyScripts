import requests

uber_uuid_list=["22845a03-dbc8-4a1c-b0c4-81210952e617", "875e1293-0f11-4f40-9d7d-5e5500e098bd"]
token = "JA.VUNmGAAAAAAAEgASAAAABwAIAAwAAAAAAAAAEgAAAAAAAAHQAAAAFAAAAAAADgAQAAQAAAAIAAwAAAAOAAAApAAAABwAAAAEAAAAEAAAAHnujmCPqFL3jzIeskyAk1uAAAAA4By3Rsz6KqL5_fm1WbrbCtpWchT-A-0s_-_lADsIfeJ46S7HhNJozxEoHli4weI5hzxfhveSFnASvhoXV755KzgriI-ZgcZIuRhIMBSMOHhrKeFoxRhBkjrsjsBgj93SLcLbxJOBf9pczovMKZ9717e8zTVsMWhXULlSKKqQ9TEMAAAAXbLXRfvFePsc7nDrJAAAAGIwZDg1ODAzLTM4YTAtNDJiMy04MDZlLTdhNGNmOGUxOTZlZQ"

for uuid in uber_uuid_list:

    url = f"https://api.uber.com/v1/eats/stores/{uuid}/pos_data"

    payload={}
    headers = {
    'Authorization': f'Bearer {token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    
    if response.ok:
        jsonResponse = response.json()
        isEnabled = "Enabled" if jsonResponse.get("order_release_enabled") else "Disabled"
        print(f"Order release is {isEnabled} -> {uuid}")
    
    
    else:
        print(response.text)
    

    
def _get_uber_token(application: str) -> str:
    """
    Get uber token for a specific application
    """
    
    # Implement here