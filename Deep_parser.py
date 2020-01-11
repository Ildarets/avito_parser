import requests
from bs4 import BeautifulSoup
import time

domain = 'https://www.avito.ru'


class Deep_Parser:
    def __init__(self, url_car):
        # url_car = url_car.split('/')
        # url_car = url_car[3]
        self.url_car = url_car

    def parsing(self):

        url = f'{domain}{self.url_car}'
        # headers = {
        #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        #     'accept-encoding': 'gzip, deflate, br',
        #     'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        #     'cache-control': 'max-age=0',
        #     'cookie':'u=2jxensq2.qeepyy.gaoi14v6gq; dfp_group=91; __cfduid=d6bd71abdc4b08ce9bd817164a622cee01578417203; abp=2; buyer_tooltip_location=0; no-ssr=1; _ga=GA1.2.417231860.1578417205; _gid=GA1.2.79994371.1578417205; _ym_uid=1578417206967240838; _ym_d=1578417206; f=5.0c4f4b6d233fb90636b4dd61b04726f147e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b984dcacfe8ebe897bfa4d7ea84258c63d59c9621b2c0fa58f897baa7410138eadfb0fb526bb39450a46b8ae4e81acb9fae2415097439d4047fb0fb526bb39450a46b8ae4e81acb9fa34d62295fceb188dd99271d186dc1cd03de19da9ed218fe2d50b96489ab264edd50b96489ab264edd50b96489ab264ed46b8ae4e81acb9fa51b1fde863bf5c12f8ee35c29834d631c9ba923b7b327da71caed3f5220ce0ab6e508afc42a0695a2985db2d99140e2da661410c4c194774cc1c7e34a5a1811d38f0f5e6e0d2832e31c578b8b0849c3f2d38179306cb93218f1786dad6fd98129e82118971f2ed64956cdff3d4067aa5d6e2d2722134ea12b56ccb3c5776628a3de19da9ed218fe23de19da9ed218fe20d921840ced2a4b864a4a90450f035ac845a8aa72c58074e; _ym_isad=1; buyer_selected_search_radius0=200; luri=rossiya; buyer_popup_location=621540; __gads=ID=e4f81ab573bf2d9b:T=1578418882:S=ALNI_MbhNJUofsen2rJeCpkfXNVIx44-5A; v=1578423935; _ym_visorc_34241905=b; __utmc=99926606; __utmz=99926606.1578424166.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); buyer_location_id=621540; __utma=99926606.417231860.1578417205.1578424166.1578427263.2; __utmb=99926606.1.9.1578427263; _nfh=2822e25b57db48a293f8c5bd21e6dfbc; buyer_selected_search_radius4=0_general; _ym_visorc_106253=w; _ym_visorc_189903=w; _ym_visorc_188382=w; anid=1405519639%3B46d3b750bd4c4b9a0722229ceaaad5e2%3B1; sessid=ece320e384167f6e9a94126f3768e34c.1578427384; auth=1; sx=H4sIAAAAAAACA51VwZaqOhD8F9d30YQmNPM32EDUqAGiRLhn%2Fv1V5hy94%2BzeHBduoKiqrq7%2Bu1Mt26UeZ3t0iVlj5Kgef2n38Xe37D52s%2FNLt2ymOaQYKXgRT8mLV2Ufvd%2F92fW7j6KqpaLSFvbzz07aM020vzdnCRpi8MBTvEdPSHNPzX3v9vsmuKAADNGRx7OqGvkHpKkA2VWbr277e3eRKFFD8gmgEsMT0m2H43zu98dFmR0ziSRSJecCJ5V3SDaAtGIvm5C5L8k5SSwKWT6E%2BIScwmRNeCytCUyaNIEaVDtypJ7CN8iCyjKzbE%2Bl1vOZ5hsIuOC8xOSdyIvl2RRjuk5bcYIdGgIl51OCB4FjCOmNpdSZZXfomrIZ1h7jCXBKHGffk3tC8rBs6xia%2B3XS6Jl8xPc8eQlgS%2FEHZAnI8sqh7ubIE3GE8OAkRJ9Yn5B2qud52mRqVNQ7pQjVXjElwkC%2FsywKqrJw3ZtR12t5XnM4JEIzhaj%2FSCa7hG6r186oJhJF1pChIC7CcfpOsioqAWK1aWeNaQcr4oRjDCTRK8sTslw37oplOfd9HolSYJf1I8MpkfsOabnKuuvpeIzklvJELkEQMsQOVr2S7pul0sJ6PiLl6vAEUyCWSPBc31kazro5FUtzicPlIgTP6SsdEQ68Bs5%2BvpVjMxZKyCLnuKswZo18pPgOWXGeTmF7TnSX6h4xF0SY4D8271eQdZ33sRzD1SDpW%2FBZUVaekKb4G0imLNyuoTMPXYcZRZDyDhMckH8sL%2F3w6PfuNh1SEpYUsEGYDNBSTv7b8rDN4ymOfUu37TCDg2DeQnlzQOEXkKW1OUTFwbTGDvZQtUJAxJJLRD2430HmfSyN2dJQWr0agZeJPbrIo5F%2BI9x%2BLU9zWVcT9HS6qAakLmI2YMm%2FgSykyF7yXsvRr9u%2BSLmx8o%2BwwORf2xPaS3U%2B%2BwrNG%2FBRTA6QCAYD%2FK2BC2NNAcjeuMXcfClD%2BookFjclJJ6fkFe53Rx2Mnr0Hp7BygQsLLLL2fZ3lmWOus5UP9KB9Og0QneA9KzrlUvPox141VJdRP2KgxoUB3oolz%2B%2FQ9ovls1Rhmps2gEqUJWwM6fIvULk%2B6YWXe0B1yyBH04OLgWaIzcRvUM2JoeoncuhqGLVu0RM2EnYpHj3BdmPXXvxF3fqfL526pA1GCrZSQ7xR4iy8P5at9P5up1GnFRxPiedcFr9%2Fy%2B3oqy%2FJr5%2FLId4rfptCjHi2gIYc%2FCvpHe32KT946ELOw2EJkcFwh%2Bfz0Skd0SpPj%2F%2FA5Mo5jcaCAAA; buyer_from_page=catalog',
        #     'referer': 'https://www.avito.ru/rossiya/avtomobili',
        #     'sec-fetch-mode': 'navigate',
        #     'sec-fetch-site': 'same-origin',
        #     'sec-fetch-user': '?1',
        #     'upgrade-insecure-requests': '1',
        #     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        # }
        #
        headers = {
        'authority': 'www.avito.ru',
        'method': 'GET',
        'path': '/moskva/avtomobili/ferrari_360_2000_1775773846',
        'scheme':'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'cookie': 'u=2jxensq2.qeepyy.gaoi14v6gq; __cfduid=d6bd71abdc4b08ce9bd817164a622cee01578417203; abp=2; buyer_tooltip_location=0; no-ssr=1; _ga=GA1.2.417231860.1578417205; _gid=GA1.2.79994371.1578417205; _ym_uid=1578417206967240838; _ym_d=1578417206; buyer_selected_search_radius0=200; buyer_popup_location=621540; __gads=ID=e4f81ab573bf2d9b:T=1578418882:S=ALNI_MbhNJUofsen2rJeCpkfXNVIx44-5A; __utmc=99926606; __utmz=99926606.1578424166.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); buyer_location_id=621540; __utma=99926606.417231860.1578417205.1578424166.1578427263.2; buyer_selected_search_radius4=0_general; anid=1405519639%3B46d3b750bd4c4b9a0722229ceaaad5e2%3B1; sessid=ece320e384167f6e9a94126f3768e34c.1578427384; auth=1; v=1578502064; luri=rossiya; dfp_group=91; _ym_isad=1; f=5.0c4f4b6d233fb90636b4dd61b04726f147e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b984dcacfe8ebe897bfa4d7ea84258c63d59c9621b2c0fa58f897baa7410138ead3de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe207b7a18108a6dcd6f8ee35c29834d631c9ba923b7b327da71caed3f5220ce0ab6e508afc42a0695a2985db2d99140e2da661410c4c194774cc1c7e34a5a1811d38f0f5e6e0d2832e31c578b8b0849c3f2d38179306cb93218f1786dad6fd98129e82118971f2ed64956cdff3d4067aa5d6e2d2722134ea125c9f3514c61fd9923de19da9ed218fe23de19da9ed218fe23f9e1368ea04a10b; _ym_visorc_34241905=b; _nfh=29d918dd2b41675d804481a8e3c76dd6; _ym_visorc_106253=w; _ym_visorc_189903=w; _ym_visorc_188382=w; sx=H4sIAAAAAAACA51WwXKjOhD8F5%2F3MMAAw%2F4NDCCwbI%2BNHATeyr%2B%2FVl7Fife2qVRucqunu6fFn0Ml1fkhlL%2Bt0TmJLErRe7Nw%2BP3nsB5%2BH6rB3q750DSNGQcLImzeOYoOh50cfh2Gw%2B%2BsrKXMKmro%2FdehPRZaLyda7szkzHkJ0TsR%2B4TM5uI2vXHZTOegAkDgSBD1plHYvUJKAcjiwlb3S%2BAbcQBLc2LBR9Yny1u9LLeH3BoFjlMKqs4DMZAA9TtkRmUJyGq3Pt90HxfxGg08SAhU6RPyPIzb0Ln7bYpgJdFIcWG0GKKI2ndI4iqxzOahpftjWpRIQjChNLXFn0AWVSUJcsrbvBqrqWyFgAjNJTA79zPIPGmZ5484FpVecmGyyN7geFD7yeDVh5bNed9z0%2BPxrGrO%2BRCjgSX%2FBDKTLGnJnRZXvz%2B6LHpYmf4IfpL%2FhAz53R5hXx83Mw9pktyiGsQk%2BfgNsuFGGkAOuVvzuy9kjDCIQsDg0ZPyJ%2BRF7nf34D54ZBZnlNW8clDMAtlfWRYMSF2o3uJEOjsNmNsweprruT2er9XIuxbqgsYgDtNExgEME4RfIasssWxmGctr047K3rFCzpQi9wyRH5padK%2BmCeqBnymyGx1IYyB6hWzyFKJ2KcasDOXgIjFBIfVR8dsn5HDt27M%2Fu2MPuGDqkDWHjYRNMDH8FaI0%2BHCp29vp8jheY8BUPiWdyPzTnmKHkNm6noYBzmEhjcGPiSFPpJcdL%2BoPx7ttncKlHGBoCAEUQ%2FLBP5Pe30MTu23TlZ0aYbGjJn28MeJLr4iSYlm6tRyOBfU3dFqA2WpRHNLyCXlbqk36eD9vmmovEHxHsSiscsG9zF1BzJT0TE6Wa2NbQBOpx7%2BBiz2TPk1z341CbRYcrooMULQfiXgvr%2B5UeZ1Y1uOW75dFe%2BA4DsiHh%2FhQ6ROy66r9dFpsP3pn8EMwtmBrHWSClS%2BQ5YeU1yHPGyum4xksI6JpEaH88tuv52v%2F6IZ99KlxTVKhe3ZpcZheOr3OPyJUhGUu1%2Fx0mmdDdMXD7NTVT5L5aV39dHdWKBuZsoPfFBW7HrznV0hJQZdiDm%2FXKSu6dClC5BTm2JfhTup2XPfRjhywjUBDfIgNXY1Z3CtklqoNhdtt1B07BrlUCRDJGL4%2Fe8g%2Fjlxxse9JEXgdkR7sLTtQ9voKySnoxTA112HL7pXDXIQmgD0ooueGtzVVcZjPQ%2B%2BZkyOCLmXcioX37vvLgyKqq7Q7tvKan3e8t0weJRhT3UR5aqlDflu67Xwf8dgJMuRiUhMOIsXh%2B%2BAVwZ%2B0O0xds3QuH9L6CicmUDXIE1LavHmsc409RBxwgNONOIKN%2FBvyY8NFedSiKmFyKutUQYmGf0Ie%2B%2F7UWhHmCrHByER4xwGOi6Hqd8Ts%2Fwz12Ta3i5wWcpQOIyJYoPj1SvwLItfpkdicnK8V31AGCDrCEfH6B3P%2FjNhwkaVvl2YY1tpfKPSoatYUYywEf70R96XM%2B3xp9zcBBsxGFSGbeEURd2d%2FPTvJmyzc7HJ79HNzxzdTwKcB%2FMZDpV%2F7PYS3Msz28dQppBZNrqdOci%2BhbEqi%2FP39PwwKygi2CQAA; so=1578508602; buyer_from_page=catalog',
        'referer': 'https://www.avito.ru/rossiya/avtomobili/ferrari?cd=1',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        }
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
        # print(url)
        return parameters_car
        # return url
