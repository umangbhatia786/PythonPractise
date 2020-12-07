
import requests
api_url = 'https://reqres.in/api/users/2'
response = requests.get(api_url, headers = {'Accept': 'application/json'})

print(f'Request to {api_url} returned status code {response.status_code}')

data = response.json()

print(f'User\'s id is {data["data"]["id"]} and email is {data["data"]["email"]}')