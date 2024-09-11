# requests kutuphanesi HTTP istekleri yapmamıza olanak tanır
import requests

# get request

url = "https://httpbin.org/get"

response = requests.get(url)

print(response)
print(type(response))
print(f"status code {response.status_code}")


if response.status_code == 200:
    print("istek basarılı")
else:
    print("istekbasarısız")

# response içeriği
print(response.text)
print(type(response.text))

# response json formatı
data = response.json()  # json converter

print(data)
print(type(data))

# parametreler ile get req
# get req parametre ekleyerek özelleşmiş istek atma

res = requests.get(url, params={"user": "aras", "password": "123456"})
print(f"status code {res.status_code}")

# farklı bir url'e get req gönderme
url1 = "https://www.amazon.com.tr"
url2 = "https://tr.wikipedia.org/wiki/Trabzon"

res1 = requests.get(url1)
print(res1)

res1_text = res1.text
print(res1_text[:80])

res2 = requests.get(url2)
print(res2)
res2_text = res2.text
print(res2_text[:100])

