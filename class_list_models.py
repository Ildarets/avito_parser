import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth
from bs4 import BeautifulSoup
import pprint
import time

class List_Models:
    def list_models(self):
        list_models = []
        domain = 'https://www.avito.ru/rossiya/avtomobili'
        url_model = 'baw'

        # url = f'{domain}/{url_model}?p={number_page}'
        url = 'https://www.avito.ru/rossiya/avtomobili?cd=1'
        # response = requests.get(url,auth = HTTPDigestAuth('ildarets@mail.ru', 'FOEnO8b6p979pM'))

        headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'cookie':'u=2jxensq2.qeepyy.gaoi14v6gq; dfp_group=91; __cfduid=d6bd71abdc4b08ce9bd817164a622cee01578417203; abp=2; buyer_tooltip_location=0; no-ssr=1; _ga=GA1.2.417231860.1578417205; _gid=GA1.2.79994371.1578417205; _ym_uid=1578417206967240838; _ym_d=1578417206; f=5.0c4f4b6d233fb90636b4dd61b04726f147e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b984dcacfe8ebe897bfa4d7ea84258c63d59c9621b2c0fa58f897baa7410138eadfb0fb526bb39450a46b8ae4e81acb9fae2415097439d4047fb0fb526bb39450a46b8ae4e81acb9fa34d62295fceb188dd99271d186dc1cd03de19da9ed218fe2d50b96489ab264edd50b96489ab264edd50b96489ab264ed46b8ae4e81acb9fa51b1fde863bf5c12f8ee35c29834d631c9ba923b7b327da71caed3f5220ce0ab6e508afc42a0695a2985db2d99140e2da661410c4c194774cc1c7e34a5a1811d38f0f5e6e0d2832e31c578b8b0849c3f2d38179306cb93218f1786dad6fd98129e82118971f2ed64956cdff3d4067aa5d6e2d2722134ea12b56ccb3c5776628a3de19da9ed218fe23de19da9ed218fe20d921840ced2a4b864a4a90450f035ac845a8aa72c58074e; _ym_isad=1; buyer_selected_search_radius0=200; luri=rossiya; buyer_popup_location=621540; __gads=ID=e4f81ab573bf2d9b:T=1578418882:S=ALNI_MbhNJUofsen2rJeCpkfXNVIx44-5A; v=1578423935; _ym_visorc_34241905=b; __utmc=99926606; __utmz=99926606.1578424166.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); buyer_location_id=621540; __utma=99926606.417231860.1578417205.1578424166.1578427263.2; __utmb=99926606.1.9.1578427263; _nfh=2822e25b57db48a293f8c5bd21e6dfbc; buyer_selected_search_radius4=0_general; _ym_visorc_106253=w; _ym_visorc_189903=w; _ym_visorc_188382=w; anid=1405519639%3B46d3b750bd4c4b9a0722229ceaaad5e2%3B1; sessid=ece320e384167f6e9a94126f3768e34c.1578427384; auth=1; sx=H4sIAAAAAAACA51VwZaqOhD8F9d30YQmNPM32EDUqAGiRLhn%2Fv1V5hy94%2BzeHBduoKiqrq7%2Bu1Mt26UeZ3t0iVlj5Kgef2n38Xe37D52s%2FNLt2ymOaQYKXgRT8mLV2Ufvd%2F92fW7j6KqpaLSFvbzz07aM020vzdnCRpi8MBTvEdPSHNPzX3v9vsmuKAADNGRx7OqGvkHpKkA2VWbr277e3eRKFFD8gmgEsMT0m2H43zu98dFmR0ziSRSJecCJ5V3SDaAtGIvm5C5L8k5SSwKWT6E%2BIScwmRNeCytCUyaNIEaVDtypJ7CN8iCyjKzbE%2Bl1vOZ5hsIuOC8xOSdyIvl2RRjuk5bcYIdGgIl51OCB4FjCOmNpdSZZXfomrIZ1h7jCXBKHGffk3tC8rBs6xia%2B3XS6Jl8xPc8eQlgS%2FEHZAnI8sqh7ubIE3GE8OAkRJ9Yn5B2qud52mRqVNQ7pQjVXjElwkC%2FsywKqrJw3ZtR12t5XnM4JEIzhaj%2FSCa7hG6r186oJhJF1pChIC7CcfpOsioqAWK1aWeNaQcr4oRjDCTRK8sTslw37oplOfd9HolSYJf1I8MpkfsOabnKuuvpeIzklvJELkEQMsQOVr2S7pul0sJ6PiLl6vAEUyCWSPBc31kazro5FUtzicPlIgTP6SsdEQ68Bs5%2BvpVjMxZKyCLnuKswZo18pPgOWXGeTmF7TnSX6h4xF0SY4D8271eQdZ33sRzD1SDpW%2FBZUVaekKb4G0imLNyuoTMPXYcZRZDyDhMckH8sL%2F3w6PfuNh1SEpYUsEGYDNBSTv7b8rDN4ymOfUu37TCDg2DeQnlzQOEXkKW1OUTFwbTGDvZQtUJAxJJLRD2430HmfSyN2dJQWr0agZeJPbrIo5F%2BI9x%2BLU9zWVcT9HS6qAakLmI2YMm%2FgSykyF7yXsvRr9u%2BSLmx8o%2BwwORf2xPaS3U%2B%2BwrNG%2FBRTA6QCAYD%2FK2BC2NNAcjeuMXcfClD%2BookFjclJJ6fkFe53Rx2Mnr0Hp7BygQsLLLL2fZ3lmWOus5UP9KB9Og0QneA9KzrlUvPox141VJdRP2KgxoUB3oolz%2B%2FQ9ovls1Rhmps2gEqUJWwM6fIvULk%2B6YWXe0B1yyBH04OLgWaIzcRvUM2JoeoncuhqGLVu0RM2EnYpHj3BdmPXXvxF3fqfL526pA1GCrZSQ7xR4iy8P5at9P5up1GnFRxPiedcFr9%2Fy%2B3oqy%2FJr5%2FLId4rfptCjHi2gIYc%2FCvpHe32KT946ELOw2EJkcFwh%2Bfz0Skd0SpPj%2F%2FA5Mo5jcaCAAA; buyer_from_page=catalog',
        'referer': 'https://www.avito.ru/rossiya/avtomobili',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        # response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # print(soup)

        avtos = soup.find_all('a', class_ = 'popular-rubricator-link-3112O')

        # print(avtos)
        time.sleep(0.1)
        for avto in avtos:
            href = avto.get('href')
            # title = avto.get('title')
            href = href.split('/')
            href = href[3]
            href = href.split('?')
            href = href[0]
            list_models.append(href)

        return list_models