import requests
import json
from jsonpath import jsonpath

base_url = 'https://reqres.in/api/users'
id = 506

api_url = '{}/{}'.format(base_url, id)

with open(r'APITesting\PUT\update_user.json') as file:
    json_input = file.read()

request_json = json.loads(json_input)
res = requests.put(api_url, request_json)
print(f'Request returned Response Code: {res.status_code}')
res_json = json.loads(res.text)

#Fetching required values from the json
updated_name = jsonpath(res_json, 'name')
updated_job = jsonpath(res_json, 'job')

#Validating Response Code and Response values
assert res.status_code == 200
assert updated_name == jsonpath(request_json, 'name')
assert updated_job == jsonpath(request_json, 'job')

