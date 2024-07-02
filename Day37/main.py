import requests
from datetime import datetime

today = datetime.today().strftime('%Y%m%d')

USERNAME = "johlstrom"
TOKEN = "XXXXXXXXXXXXXXXXXX"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph0",
    "name": "Coding",
    "unit": "Minutes",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_endpoint = f"{graph_endpoint}/{graph_config['id']}"

post_config = {
    "date": today,
    "quantity": "75"
}

# response = requests.post(url=post_endpoint, json=post_config, headers=headers)
# print(response.text)