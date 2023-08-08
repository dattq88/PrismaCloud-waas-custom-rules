import requests

url = 'http://52.163.96.252:8088/'
headers = {'User-Agent': 'zerodiumsystem'}

response = requests.get(url, headers=headers)

if 'Access denied' in response.text:
    print("Access denied")
else:
    print("Access granted")
