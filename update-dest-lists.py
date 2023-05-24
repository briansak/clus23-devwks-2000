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

def update_dest_list(token):

    destinationListId = YOUR_DEST_LIST_ID
    url = f"https://api.umbrella.com/policies/v2/destinationlists/{destinationListId}/destinations"
    
    payload = '''[
    { "destination": "streamingsite.com" },
    { "destination": "gambling.com" },
    { "destination": "internetbadguys.com" }
    ]
    '''
    
    headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {token}"
    }

    response = requests.request('POST', url, headers=headers, data = payload)

    print(response.json())

token = get_token()
update_dest_list(token)
