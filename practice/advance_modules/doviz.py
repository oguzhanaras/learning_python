import requests
import sys

# Fixer API key'inizi buraya ekleyin
api_key = "YOUR_API_KEY"
url = f"http://data.fixer.io/api/latest?access_key={api_key}&base="

birinci_doviz = input("Birinci Döviz (örn. EUR): ").upper()
ikinci_doviz = input("İkinci Döviz (örn. USD): ").upper()

try:
    miktar = float(input("Miktar: "))
except ValueError:
    sys.stderr.write("Lütfen geçerli bir miktar girin\n")
    sys.stderr.flush()
    sys.exit()

# API isteği gönder
response = requests.get(url + birinci_doviz)
json_verisi = response.json()

# API'nin başarılı bir cevap dönüp dönmediğini kontrol edin
if response.status_code != 200 or not json_verisi['success']:
    sys.stderr.write("API isteği başarısız oldu. Lütfen tekrar deneyin.\n")
    sys.stderr.flush()
    sys.exit()

try:
    doviz_kuru = json_verisi["rates"][ikinci_doviz]
    print(f"{miktar} {birinci_doviz}, {doviz_kuru * miktar:.2f} {ikinci_doviz} eder.")
except KeyError:
    sys.stderr.write("Lütfen para birimlerini doğru girin\n")
    sys.stderr.flush()
