import requests
from bs4 import BeautifulSoup
import time

domain = 'https://www.avito.ru'


class Deep_Parser:
    def __init__(self, url_car):
        self.url_car = url_car

    def parsing(self):

        url = f'{domain}{self.url_car}'
        headers = {
        'authority': 'www.avito.ru',
        'method': 'GET',
        'path': '/moskva/avtomobili/ferrari_360_2000_1775773846',
        'scheme':'https',
        'accept': 'ext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'cookie': 'u=2jz6x3tn.ot9948.gbx8z94gis; __cfduid=d9f8be2869150d70f00b679b5542a54041581761435; buyer_selected_search_radius0=200; _ga=GA1.2.575084678.1581761446; _gid=GA1.2.1061643092.1581761446; buyer_tooltip_location=0; _ym_uid=1573753899360583882; _ym_d=1581761451; sessid=cd575aa2a65cba3b5af23ca42ef5317c.1581863787; abp=2; no-ssr=1; f=5.0c4f4b6d233fb90636b4dd61b04726f147e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b91772440e04006def90d83bac5e6e82bd59c9621b2c0fa58f897baa7410138ead3de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe207b7a18108a6dcd6f8ee35c29834d631c9ba923b7b327da71caed3f5220ce0ab049e6584365a0f6c2985db2d99140e2db186abe826e3b1d140e001317c4d7c0e38f0f5e6e0d2832ec5987b837f8da9d1e31784d6ce1af7c75dcded8022a3c9fccbf1a5019b899285164b09365f5308e731f2b7daefd09fa0ccd5569c3c25a82e2da10fb74cac1eab2da10fb74cac1eab3069315ebaf9ae7f8012e98924060d02; _ym_isad=1; buyer_popup_location=640310; _nfh=f2147bdfa8a1446d34273c6d84ef1521; __utma=99926606.575084678.1581761446.1581867800.1581867800.1; __utmc=99926606; __utmz=99926606.1581867800.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __gads=ID=a9e34cdf279ff99f:T=1581867800:S=ALNI_MbFVuSHi5-bTyg4lijEZFNzklSU8A; buyer_selected_search_radius4=0_general; buyer_location_id=621540; luri=rossiya; sx=H4sIAAAAAAACA53STXLqMAwA4Ltk3YXsKLHCbUAEEQRjqAqCdHr3pyzog22TmWxifdbfd9NTf5oJ8vXmIuRIDK5aqzWr7%2BbWrJpuGol0RxnjL7uZoLKyiyk4ePPRjM0qdZSGkoYOfz4a3HB71se8Sa7MsrwQIaBP0sb5cbztUCfD0NBJtBKBVKyO9YXsIFEJkvc%2B8aafRqFKwCKuhBYpPEm52jYdrPT7uFKFtSKBuzBSdec3ss0pSDrkTTkd9XhmIHKvpmKRCP6Sl%2FlruOB2vntUblE8s1HU4tEgk1cSoR%2BCHHdT3Xz2pV0DEzpGGigG%2Bpslz%2BPA%2B3UtQSJU0rhYDGut0c9Kb2Rq%2ByBbaneXdb5e7qeYidcg4ySq%2F4kcFrLPN6nnlnR5JEJ8iYvp%2FoXMeSl8uy80bYc5jhMbuMkCqtCTTKkeLe%2Fbz3R3i%2B0BsFifaGV8YkqvZFcoB7nm6VC%2Bhv7yqGAShccuGdn%2FXhYcykya1wPTkj0v%2BwBQQQRE30jqYuI%2F%2FwCKk%2FoR7AIAAA%3D%3D; dfp_group=6; buyer_from_page=catalog',
        'referer': 'https://www.avito.ru/rossiya/avtomobili/ferrari?cd=1',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
        }

        # headers = {
        #     'authority': 'an.yandex.ru',
        #     'method': 'GET',
        #     'path': '/meta/189903?grab=dNCQ0LLQuNGC0L4g4oCUINC-0LHRitGP0LLQu9C10L3QuNGPINCywqDQoNC-0YHRgdC40Lgg4oCUINCe0LHRitGP0LLQu9C10L3QuNGPINC90LDCoNGB0LDQudGC0LUg0JDQstC40YLQvgoy0KDQtdC60L7QvNC10L3QtNCw0YbQuNC4INC00LvRjyDQstCw0YEgCjPQl9Cw0LPRgNGD0LfQuNGC0LUg0L_RgNC40LvQvtC20LXQvdC40LUg0JDQstC40YLQviAK&target-ref=https%3A%2F%2Fwww.avito.ru%2Frossiya&page-ref=https%3A%2F%2Fwww.avito.ru%2Fsarov&charset=utf-8&duid=MTU3ODQxNzIwNjk2NzI0MDgzOA%3D%3D&imp-id=127&partner-stat-id=100000079&enable-flat-highlight=1&test-tag=71468255805442&ss-skip-token-length=20&allow-repeat-ads=0&ad-session-id=7660661581774697345&target-id=73025066&pcode-version=10370&flash-ver=0&available-width=300&layout-config=%7B%22win_width%22%3A914%2C%22win_height%22%3A937%2C%22width%22%3A300%2C%22height%22%3A0%2C%22left%22%3A682%2C%22top%22%3A678%2C%22visible%22%3A1%2C%22ad_no%22%3A0%2C%22req_no%22%3A2%7D&callback=Ya%5B8454343842637%5D',
        #     'scheme': 'https',
        #     'accept': '*/*',
        #     'accept-encoding': 'gzip, deflate, br',
        #     'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        #     'content-type': 'application/x-www-form-urlencoded',
        #     'cookie': 'yandexuid=6807681601578082398; i=7+LmaE0F1I0LFo8p89ALQ8n5YV4frYge8n4tg2tPn0Oznn7IN7XCCjbuLM7CJ2GqgFlMHE00tY9K4XmCbELAzcxnWo4=; yp=1893442399.yrtsi.1578082399; yuidss=6807681601578082398; _ym_uid=1578255989775831569; _ym_d=1578255989; mda=0; skid=9329353061578391736; ymex=1897123244.yrts.1581763244#1893442399.yrtsi.1578082399',
        #     'origin': 'https://www.avito.ru',
        #     'referer': 'https://www.avito.ru/rossiya',
        #     'sec-fetch-dest': 'empty',
        #     'sec-fetch-mode': 'cors',
        #     'sec-fetch-site': 'cross-site',
        #     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
        # }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        parameters_car = {}
        price_soup = soup.find('span', class_='js-item-price')
        try:
            price_car = price_soup.get('content')
        except AttributeError:
            price_car = 'None'

        parameters_car['price'] = price_car
        time.sleep(0.1)
        parameters = soup.find_all('li', class_='item-params-list-item')
        for child in parameters:
            child = child.get_text()
            child = child.split(': ')
            child_name = str(child[0].replace(' ', ''))
            child_param = str(child[1].replace(' ', ''))
            parameters_car[child_name] = child_param
        return parameters_car
