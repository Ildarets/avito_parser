import requests
from bs4 import BeautifulSoup
import time

domain = 'https://hidemy.name/ru/proxy-list/'

class Proxy_Parser:
    # def __init__(self, url_car):
    #     self.url_car = url_car

    def parsing(self):

        url = f'{domain}'
        # headers = {
        #     'Accept-Encoding': 'gzip, deflate, br',
        #     'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        #     'Cache-Control': 'no-cache',
        #     'Connection': 'Upgrade',
        #     'Host': 'chat5-1.jivosite.com',
        #     'Origin': 'https://hidemy.name',
        #     'Pragma': 'no-cache',
        #     'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits',
        #     'Sec-WebSocket-Key': 'frFARggb+9TsWv/GN4EoPQ==',
        #     'Sec-WebSocket-Version': '13',
        #     'Upgrade': 'websocket',
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
        # }
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        list_proxy = []
        soup_proxy = soup.find_all('div', class_='table_block')
        # proxy = soup.get_text()

        # parameters_car['price'] = price_car
        # time.sleep(0.1)
        # parameters = soup.find_all('li', class_='item-params-list-item')
        # for child in parameters:
        #     child = child.get_text()
        #     child = child.split(': ')
        #     child_name = str(child[0].replace(' ', ''))
        #     child_param = str(child[1].replace(' ', ''))
        #     parameters_car[child_name] = child_param
        return soup
