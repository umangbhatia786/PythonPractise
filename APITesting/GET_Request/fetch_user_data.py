import requests
import json
from jsonpath import jsonpath

#API URL
api_url = 'https://reqres.in/api/users?page=2'

#GET Request
res = requests.get(api_url)

#Displaying response content
print(res.content)
print(res.status_code)
print(res.headers)

#Parse response to JSON
json_response = json.loads(res.text)
print(json_response)

pages = jsonpath(json_response, 'total_pages')

assert pages[0] == 2



