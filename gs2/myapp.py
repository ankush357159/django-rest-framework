import requests
import json

URL = "http://localhost:8000/stucreate/"

data = {
    'name': 'Dhiraj',
    'roll': 123,
    'city': 'Navi Mumbai'
}

json_data = json.dumps(data)
r = requests.post(url = URL, data=json_data)
data = r.json()
print(data)


