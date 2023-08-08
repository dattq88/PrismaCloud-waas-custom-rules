#file để test xem headder no anchua

import requests

url = 'http://52.163.96.252:8088/'
headers = {'User-Agentt': 'zerodiumsystem'} #headers = {'User-Agentt': 'zerodiumsystem'}

response = requests.get(url, headers=headers)

if 'Access denied' in response.text:
    print("Access denied")
else:
    print("Access granted")

