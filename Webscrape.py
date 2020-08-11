import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as urec
from lxml import html

#Uses the url and requests access to the site
url = "https://www.microcenter.com/category/4294966937/Video-Cards"
web = urec(url)
#Reads the website data in 
page_html = web.read()
web.close()
#Creates a beautiful soup object to parse the data in the website
soup = bs(page_html, "html.parser")
#print(soup.prettify())

#Finds all the details of the products on the page
details = soup.findAll('div', class_='details')
#print(len(details))


detail = details[0]
#Finds the price of one product
detail.find("div", {'class':'price'}).text.strip()

#Finds the name of one product 
normal = detail.find("div", {'class': 'normal'})
normal.a['data-name']

#Finds the availability of one product 
detail.find('p', {'class': 'availabilityTrunc'}).text

#Creats a file to write in the values parsed from the website 
filename = "video-cards.csv"
headers = "Price, Name, Availability\n"
f = open(filename, "w")
f.write(headers)

#Creates a loop to go through every product on the page 
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



