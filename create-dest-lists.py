import requests
from requests.auth import HTTPBasicAuth
import json

def get_token():
    key = 'YOUR_KEY'
    secret = 'YOUR_SECRET'
    
    url = "https://api.umbrella.com/auth/v2/token"
    
    payload = None
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        }
        
    token = requests.request('POST', url, headers=headers, data=payload, auth=HTTPBasicAuth(key, secret))
    return token.json()['access_token']

def create_dest_list(token):

    url = "https://api.umbrella.com/policies/v2/destinationlists"
    
    payload = '''{
    "access": "block",
    "isGlobal": false,
    "name": "SWG Destination List YOUR_POD"}
    '''

    headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {token}"
    }

    response = requests.request('POST', url, headers=headers, data = payload)

    print(f'Your Destination List ID is: {response.json()["id"]}')

token = get_token()
create_dest_list(token)
