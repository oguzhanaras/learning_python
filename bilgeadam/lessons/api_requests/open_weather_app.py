import requests

api_key = "your_api_key"

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "lat": 39.875, # Enlem
    "lon": 32.749, # Boylam
    "appid": api_key,   # API anahtarı
    "units": "metric"    # metric: Celcius, standard: Kelvin, Imperial: Fahrenheit
}

res = requests.get(url, params=params)
print(res.status_code)
print(res.url)

data = res.json()

print(f"Weather Description for {data.get('name')}:", end=" ")
print(data["weather"][0]["description"].title())

round(data["main"]["temp"])

# Şehir ismi

city_name = "Sydney"

url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"

res = requests.get(url, params=params)
print(res.status_code)
print(res.url)



