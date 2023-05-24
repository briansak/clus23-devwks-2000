import requests
from requests.auth import HTTPBasicAuth
import json
import csv

def get_token():
    key = 'YOUR_CLIENT_KEY'
    secret = 'YOUR_SECRET_KEY'
    
    url = "https://api.umbrella.com/auth/v2/token"
    
    payload = None
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        }
        
    token = requests.request('POST', url, headers=headers, data=payload, auth=HTTPBasicAuth(key, secret))
    return token.json()['access_token']

def create_tunnels(token):

    pod = "POD_NUMBER"

    with open('tunnels.csv', mode='r') as csv_file:
        networks = csv.DictReader(csv_file)

        for network in networks:

            url = "https://api.umbrella.com/deployments/v2/tunnels"
            city = f"{network['City']} Pod {pod}"
            cidr = network['Netblock']
            device = network['Device']

            payload = {
            "transport": { "protocol": "IPSEC" },
            "authentication": {
                "parameters": {
                    "idPrefix": f"cluspod{pod}",
                    "secret": "Secret1234567890"
                },
                "type": "PSK"
            },
            "networkCIDRs": [f"{cidr}"],
            "serviceType": "SIG",
            "deviceType": "ASA",
            "name": f"{city}",
            "deviceType": f"{device}"
            }

            headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {token}"
            }

            response = requests.request('POST', url, headers=headers, data=json.dumps(payload))
            print(response.json())

token = get_token()
tunnels = create_tunnels(token)
