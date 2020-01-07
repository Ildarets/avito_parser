import requests
from bs4 import BeautifulSoup
import pprint

domain = 'https://www.avito.ru/rossiya/avtomobili'
url_model = 'great_wall'
number_page = 1
# url = f'{domain}/{url_model}?cd={number_page}'
url = 'https://auto.ru/sarov/cars/vaz/all/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup)

avtos = soup.find_all('a', class_ = 'ListingItemTitle-module__container ListingItem-module__title')

print(avtos)

# for avto in avtos:
#     href = avto.get('href')
#     title = avto.get('title')
#     print(href, title)
