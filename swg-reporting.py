import requests
from requests.auth import HTTPBasicAuth
import datetime
import calendar

def get_token():

    key = 'YOUR_CLIENT_ID'
    secret = 'YOUR_CLIENT_SECRET'

    url = "https://api.umbrella.com/auth/v2/token"

    payload = None

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        }

    token = requests.request('POST', url, headers=headers, data=payload, auth=HTTPBasicAuth(key, secret))
    return token.json()['access_token']

def swg_report(token):
  
    end = 'now'
    start = '-7days'

    url = f"https://api.umbrella.com/reports/v2/top-destinations/proxy?from={start}&to={end}&limit=10&offset=0"

    headers = {
    'Authorization': f'Bearer {token}'
    }

    response = requests.request("GET", url, headers=headers)

    for item in response.json()["data"]:
        print (f'{item["domain"]: <50}', f'{item["categories"][0]["label"]: <30}', f'{item["count"]: <5}')

token = get_token()
swg = swg_report(token)
