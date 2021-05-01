import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

url = 'https://csgostash.com/weapon/AK-47'

response = requests.get(url, headers = headers).text

page_soup = BeautifulSoup(response, "html.parser")

Skins = page_soup.findAll("div", {"class":"col-lg-4 col-md-6 col-widen text-center"})
Rarity = page_soup.findAll("a", {"class":"nounderline"})
Price_raw = page_soup.findAll("div", {"class":"price"})

l = len(Price_raw)
Price = []
for i in range(0, l, 2):
    Price.append(Price_raw[i])

size = len(Rarity)

filename = "AK47.csv"
f = open(filename, "w")
headers = "Name, Colour, Price, Price_Range\n"
f.write(headers)
for i in range(size):
    skin = Skins[i].div.h3.a.text
    colour = str(Rarity[i].div.p.text)
    colour = colour.split(' ')[0]
    price_range = str(Price[i].p.a)
    price_range = price_range.split('>')[1]
    price_range = price_range.split('<')[0]
    price_range = price_range.replace('₹', '')
    price_range = price_range.replace(',', '')
    price = price_range.split(' ')[2]
    price = int(price.replace(',', ''))
    f.write(skin + "," + colour + "," + str(price) + "," + price_range + "\n")
f.close()