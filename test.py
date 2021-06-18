import requests

BASE = "http://127.0.0.1:5000/"
# get requ
response = requests.get(BASE + '/sairam')
# postResponse = requests.post(BASE)

print(response.json())