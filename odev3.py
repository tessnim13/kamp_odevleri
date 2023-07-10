import requests
from bs4 import BeautifulSoup

r = requests.get("https://uzmanpara.milliyet.com.tr/canli-borsa/")
r.content

soup = BeautifulSoup(r.content, "html.parser")


dolar_degeri = soup.find_all("span", {"id":"usd_header_son_data"})
euro_degeri = soup.find_all("span", {"id":"eur_header_son_data"})
altin_degeri = soup.find_all("span", {"id":"gld_header_son_data"})
petrol_degeri = soup.find_all("span", {"id":"petrol_header_son_data"})
bitcoin_degeri = soup.find_all("span", {"id":"btc_header_son_data"})

for deger in dolar_degeri:
    print("Dolar:", deger.text)
for deger in euro_degeri:
    print("Euro:", deger.text)
for deger in altin_degeri:
    print("Altın:", deger.text)
for deger in petrol_degeri:
    print("Petrol:", deger.text)
for deger in bitcoin_degeri:
    print("Bitcoin:", deger.text)


