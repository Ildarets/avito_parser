import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth
from bs4 import BeautifulSoup
import pprint
import time

class List_Models:
    def list_models(self):
        list_models = []
        url = 'https://www.avito.ru/rossiya/avtomobili?cd=1'
        headers = {
            'authority': 'www.avito.ru',
            'method': 'GET',
            'path': '/moskva/avtomobili/ferrari_360_2000_1775773846',
            'scheme': 'https',
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
        #     'authority': 'www.avito.ru',
        #     'method': 'GET',
        #     'path': '/moskva/avtomobili/ferrari_360_2000_1775773846',
        #     'scheme': 'https',
        #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        #     'accept-encoding': 'gzip, deflate, br',
        #     'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        #     'cache-control': 'max-age=0',
        #     'cookie': 'u=2jxensq2.qeepyy.gaoi14v6gq; __cfduid=d6bd71abdc4b08ce9bd817164a622cee01578417203; abp=2; buyer_tooltip_location=0; no-ssr=1; _ga=GA1.2.417231860.1578417205; _gid=GA1.2.79994371.1578417205; _ym_uid=1578417206967240838; _ym_d=1578417206; buyer_selected_search_radius0=200; buyer_popup_location=621540; __gads=ID=e4f81ab573bf2d9b:T=1578418882:S=ALNI_MbhNJUofsen2rJeCpkfXNVIx44-5A; __utmc=99926606; __utmz=99926606.1578424166.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); buyer_location_id=621540; __utma=99926606.417231860.1578417205.1578424166.1578427263.2; buyer_selected_search_radius4=0_general; anid=1405519639%3B46d3b750bd4c4b9a0722229ceaaad5e2%3B1; sessid=ece320e384167f6e9a94126f3768e34c.1578427384; auth=1; v=1578502064; luri=rossiya; dfp_group=91; _ym_isad=1; f=5.0c4f4b6d233fb90636b4dd61b04726f147e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b984dcacfe8ebe897bfa4d7ea84258c63d59c9621b2c0fa58f897baa7410138ead3de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe207b7a18108a6dcd6f8ee35c29834d631c9ba923b7b327da71caed3f5220ce0ab6e508afc42a0695a2985db2d99140e2da661410c4c194774cc1c7e34a5a1811d38f0f5e6e0d2832e31c578b8b0849c3f2d38179306cb93218f1786dad6fd98129e82118971f2ed64956cdff3d4067aa5d6e2d2722134ea125c9f3514c61fd9923de19da9ed218fe23de19da9ed218fe23f9e1368ea04a10b; _ym_visorc_34241905=b; _nfh=29d918dd2b41675d804481a8e3c76dd6; _ym_visorc_106253=w; _ym_visorc_189903=w; _ym_visorc_188382=w; sx=H4sIAAAAAAACA51WwXKjOhD8F5%2F3MMAAw%2F4NDCCwbI%2BNHATeyr%2B%2FVl7Fife2qVRucqunu6fFn0Ml1fkhlL%2Bt0TmJLErRe7Nw%2BP3nsB5%2BH6rB3q750DSNGQcLImzeOYoOh50cfh2Gw%2B%2BsrKXMKmro%2FdehPRZaLyda7szkzHkJ0TsR%2B4TM5uI2vXHZTOegAkDgSBD1plHYvUJKAcjiwlb3S%2BAbcQBLc2LBR9Yny1u9LLeH3BoFjlMKqs4DMZAA9TtkRmUJyGq3Pt90HxfxGg08SAhU6RPyPIzb0Ln7bYpgJdFIcWG0GKKI2ndI4iqxzOahpftjWpRIQjChNLXFn0AWVSUJcsrbvBqrqWyFgAjNJTA79zPIPGmZ5484FpVecmGyyN7geFD7yeDVh5bNed9z0%2BPxrGrO%2BRCjgSX%2FBDKTLGnJnRZXvz%2B6LHpYmf4IfpL%2FhAz53R5hXx83Mw9pktyiGsQk%2BfgNsuFGGkAOuVvzuy9kjDCIQsDg0ZPyJ%2BRF7nf34D54ZBZnlNW8clDMAtlfWRYMSF2o3uJEOjsNmNsweprruT2er9XIuxbqgsYgDtNExgEME4RfIasssWxmGctr047K3rFCzpQi9wyRH5padK%2BmCeqBnymyGx1IYyB6hWzyFKJ2KcasDOXgIjFBIfVR8dsn5HDt27M%2Fu2MPuGDqkDWHjYRNMDH8FaI0%2BHCp29vp8jheY8BUPiWdyPzTnmKHkNm6noYBzmEhjcGPiSFPpJcdL%2BoPx7ttncKlHGBoCAEUQ%2FLBP5Pe30MTu23TlZ0aYbGjJn28MeJLr4iSYlm6tRyOBfU3dFqA2WpRHNLyCXlbqk36eD9vmmovEHxHsSiscsG9zF1BzJT0TE6Wa2NbQBOpx7%2BBiz2TPk1z341CbRYcrooMULQfiXgvr%2B5UeZ1Y1uOW75dFe%2BA4DsiHh%2FhQ6ROy66r9dFpsP3pn8EMwtmBrHWSClS%2BQ5YeU1yHPGyum4xksI6JpEaH88tuv52v%2F6IZ99KlxTVKhe3ZpcZheOr3OPyJUhGUu1%2Fx0mmdDdMXD7NTVT5L5aV39dHdWKBuZsoPfFBW7HrznV0hJQZdiDm%2FXKSu6dClC5BTm2JfhTup2XPfRjhywjUBDfIgNXY1Z3CtklqoNhdtt1B07BrlUCRDJGL4%2Fe8g%2Fjlxxse9JEXgdkR7sLTtQ9voKySnoxTA112HL7pXDXIQmgD0ooueGtzVVcZjPQ%2B%2BZkyOCLmXcioX37vvLgyKqq7Q7tvKan3e8t0weJRhT3UR5aqlDflu67Xwf8dgJMuRiUhMOIsXh%2B%2BAVwZ%2B0O0xds3QuH9L6CicmUDXIE1LavHmsc409RBxwgNONOIKN%2FBvyY8NFedSiKmFyKutUQYmGf0Ie%2B%2F7UWhHmCrHByER4xwGOi6Hqd8Ts%2Fwz12Ta3i5wWcpQOIyJYoPj1SvwLItfpkdicnK8V31AGCDrCEfH6B3P%2FjNhwkaVvl2YY1tpfKPSoatYUYywEf70R96XM%2B3xp9zcBBsxGFSGbeEURd2d%2FPTvJmyzc7HJ79HNzxzdTwKcB%2FMZDpV%2F7PYS3Msz28dQppBZNrqdOci%2BhbEqi%2FP39PwwKygi2CQAA; so=1578508602; buyer_from_page=catalog',
        #     'referer': 'https://www.avito.ru/rossiya/avtomobili/ferrari?cd=1',
        #     'sec-fetch-mode': 'navigate',
        #     'sec-fetch-site': 'same-origin',
        #     'sec-fetch-user': '?1',
        #     'upgrade-insecure-requests': '1',
        #     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        # }
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

        avtos = soup.find_all('a', class_ = 'popular-rubricator-link-3112O')

        time.sleep(0.1)
        for avto in avtos:
            href = avto.get('href')
            href = href.split('/')
            href = href[3]
            href = href.split('?')
            href = href[0]
            list_models.append(href)

        non_duplicate = list(set(list_models))
        all_list_models = non_duplicate
        all_list_models = sorted(all_list_models)
        return all_list_models