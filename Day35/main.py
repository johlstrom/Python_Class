import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get('OWM_API_KEY')
print(api_key)
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
print(account_sid)
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
print(auth_token)

weather_params = {
    "lat": 59.329323,
    "lon": 18.068581,
    "appid": api_key,
    "units": "metric",
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remeber to bring an ☂️",
        from_='whatsapp:+16503962863',
        to='whatsapp:+46708919179'
    )
    print(message.sid)
