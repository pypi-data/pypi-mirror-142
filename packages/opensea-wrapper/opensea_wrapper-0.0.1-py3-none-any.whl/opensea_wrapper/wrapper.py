import requests
import time

base_url = 'https://api.opensea.io/api/v1'


def get_collection(collection, api_key=None):
    """Get collection from opensea

    Args:
        collection (str): collection name
    """
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    if api_key: headers = {'X-API-KEY': api_key}

    url = f'{base_url}/collection/{collection}'
    response = None
    repeat = True

    while repeat:
        response = requests.get(url, headers)

        if response.status_code != 200:
            time.sleep(1)
            print(response.json())
            continue

        response = response.json()
        repeat = False

    return response
