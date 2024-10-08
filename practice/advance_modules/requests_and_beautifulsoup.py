import requests
from bs4 import BeautifulSoup

url = "https://tr.wikipedia.org/wiki/Mustafa_Kemal_Atat%C3%BCrk"
response = requests.get(url)

print(response)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi, "html.parser")

print(soup.prettify())
print("tüm a etiketleri")
for i in soup.find_all("a"):
    print(i)
    print("*************")
