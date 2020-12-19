import requests

#API URL
api_url = 'https://reqres.in/api/users/2'

#Delete Request
res = requests.delete(api_url)

assert res.status_code == 204