import requests
import json 
from jsonpath import jsonpath
import pytest

id = ""

@pytest.mark.run(order=1)
def test_create_new_student():
    api_url = 'http://thetestingworldapi.com/api/studentsDetails'

    with open(r'C:\Users\Umang Bhatia\Documents\Udemy\Python3\APITesting\PyTest\create_new_student.json') as file:
        request_content = file.read()

    req_json = json.loads(request_content)
    res= requests.post(api_url, req_json)
    res_json = json.loads(res.text)

    assert res.status_code == 201
    global id
    id = jsonpath(res_json, 'id')[0]
    print(f'New Student Created with ID: {id}')

@pytest.mark.run(order=2)
def test_add_technical_skills():
    api_url = 'http://thetestingworldapi.com/api/technicalskills'

    with open(r'C:\Users\Umang Bhatia\Documents\Udemy\Python3\APITesting\PyTest\add_tech_skills.json') as file:
        request_content = file.read()

    req_json = json.loads(request_content)
    #setting id
    req_json['id'] = id
    req_json['st_id'] = str(id)

    res= requests.post(api_url, req_json)
    res_json = json.loads(res.text)

    msg = jsonpath(res_json, 'msg')[0]
    assert msg == "Add  data success"

@pytest.mark.run(order=3)
def test_add_address():
    api_url = 'http://thetestingworldapi.com/api/addresses'

    with open(r'C:\Users\Umang Bhatia\Documents\Udemy\Python3\APITesting\PyTest\add_address_details.json') as file:
        request_content = file.read()

    req_json = json.loads(request_content)
    #setting id
    req_json['stId'] = str(id)

    res= requests.post(api_url, req_json)
    res_json = json.loads(res.text)

    print(res.status_code)

@pytest.mark.run(order=4)
def test_get_final_student_details():
    api_url = f'http://thetestingworldapi.com/api/FinalStudentDetails/{id}'

    res= requests.get(api_url)
    res_json = json.loads(res.text)

    assert res.status_code == 500
    

