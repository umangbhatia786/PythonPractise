import requests
api_url = 'https://reqres.in/api/users'
response = requests.post(
    api_url, 
    headers = {'Accept': 'application/json'},
    params = {'name': 'Umang Bhatia', 'job': 'Test Engineering Analyst'})

print(f'Request to {api_url} returned status code {response.status_code}')

data = response.json()

for k,v in data.items():
    print(f'{k} has value {v}')