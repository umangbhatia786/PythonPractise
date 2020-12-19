import requests
import json
from jsonpath import jsonpath

api_url = api_url = 'https://reqres.in/api/users'

def test_create_new_user():
    with open(r'C:\Users\Umang Bhatia\Documents\Udemy\Python3\APITesting\POST\request.json') as file:
        json_input = file.read()

    request_json = json.loads(json_input)

    res = requests.post(api_url,request_json)

    res_json = json.loads(res.text)

    #Fetching required values from the json
    name = jsonpath(res_json, 'name')
    job = jsonpath(res_json, 'job')

    print(f'New User Created with ID: {jsonpath(res_json, "id")[0]}')

    #Validating Response Code and Response values
    assert res.status_code == 201
    assert name == jsonpath(request_json, 'name')
    assert job == jsonpath(request_json, 'job')

def test_create_other_user():
    with open(r'C:\Users\Umang Bhatia\Documents\Udemy\Python3\APITesting\POST\request.json') as file:
        json_input = file.read()

    request_json = json.loads(json_input)

    res = requests.post(api_url,request_json)

    res_json = json.loads(res.text)

    #Fetching required values from the json
    name = jsonpath(res_json, 'name')
    job = jsonpath(res_json, 'job')

    print(f'New User Created with ID: {jsonpath(res_json, "id")[0]}')

    #Validating Response Code and Response values
    assert res.status_code == 201

