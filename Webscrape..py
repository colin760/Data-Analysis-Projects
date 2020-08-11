import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as urec
from lxml import html

url = "https://www.microcenter.com/category/4294966937/Video-Cards"
web = urec(url)
page_html = web.read()
web.close()
soup = bs(page_html, "html.parser")
#print(soup.prettify())

details = soup.findAll('div', class_='details')
#print(len(details))

detail = details[0]
detail.find("div", {'class':'price'}).text.strip()
normal = detail.find("div", {'class': 'normal'})
normal.a['data-name']

detail.find('p', {'class': 'availabilityTrunc'}).text

filename = "video-cards.csv"
headers = "Price, Name, Availability\n"
f = open(filename, "w")
f.write(headers)

for detail in details:
    price = detail.find("div", {'class':'price'}).text.strip()
    
    normal = detail.find("div", {'class': 'normal'})
    name = normal.a['data-name']
    availability = detail.find('p', {'class': 'availabilityTrunc'}).text
    
    print("Price: " + price)
    print("Name: " + name)
    print("Availability: " + availability)
    
    f.write(price + "," +name + "," +availability + "\n")
f.close()

