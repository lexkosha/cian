import datetime
import time
from pprint import pprint

import requests

from src.core.db_conf import client


class DataIparchitectProxy:
    db: str = 'proxy'
    col: str = 'iparchitect_avito_pwz'
    proxy_list: list = [
        '188.143.169.29:30558:iparchitect_39067_28_05_25:5yh92zG4hntSfe8heG',
        '188.143.169.29:30566:iparchitect_39067_28_05_25:5yh92zG4hntSfe8heG',


    ]


class IparchitectProxy(DataIparchitectProxy):

    def save_ip_proxy(self):

        check_ip = requests.get(httpbin, proxies=proxy_1)
        resp = check_ip.json()

        data = {
            'resp': resp,
            'date': datetime.datetime.now()
        }
        client[self.db][self.col].insert_one(data)

    def get_proxy_in_list(self):
        proxys = list()
        for row in self.proxy_list:
            row = row.split(':')
            proxys.append(
                {'server': f'{row[0]}:{row[1]}',
                 'username': f'{row[2]}',
                 'password': f'{row[3]}'.strip()},
            )
        return proxys

    def new_ip(self, server):
        match server:

            case '188.143.169.29:30558':

                u = 'https://iparchitect.ru/api/39067/7494e91b3b9a7417c20d5f94dd142106/time/20807/change_ip/'
                requests.get(u)
                time.sleep(45)


            case '188.143.169.29:30566':
                u = 'https://iparchitect.ru/api/39067/7494e91b3b9a7417c20d5f94dd142106/time/20808/change_ip/'
                requests.get(u)
                time.sleep(45)

            case  '188.143.169.29:30530':

                u = 'https://iparchitect.ru/api/39067/7494e91b3b9a7417c20d5f94dd142106/time/20810/change_ip/'
                requests.get(u)
                time.sleep(45)

            case '188.143.169.29:30562':
                u = 'https://iparchitect.ru/api/39067/7494e91b3b9a7417c20d5f94dd142106/time/20812/change_ip/'
                requests.get(u)
                time.sleep(45)


if __name__ == '__main__':
    #31.173.81.158
    #31.173.82.39
    http_p  = 'iparchitect_39067_28_05_25:sYS5A4TarN9zYrAK2H@188.143.169.29:30562'
    https_p  = 'iparchitect_39067_28_05_25:sYS5A4TarN9zYrAK2H@188.143.169.29:30562'

    proxies = {
        'http': http_p,
        'https': https_p

    }
    request = requests.Session()
    r = request.get("https://httpbin.org/get", proxies=proxies, verify=False)
    print(
        r.json()
    )


# if __name__ == '__main__':
#     """Для теста смены ип """
#     httpbin = 'https://httpbin.org/get'
#     proxy_1 = {
#         "https": "iparchitect_39067_24_04_25:DD8nn2N9kQKrENY7QD@188.143.169.29:30578",
#         "http": "iparchitect_39067_24_04_25:DD8nn2N9kQKrENY7QD@188.143.169.29:30578"
#
#     }
#     proxy_2 = {
#         "https": "iparchitect_39067_24_04_25:DD8nn2N9kQKrENY7QD@188.143.169.29:30568",
#         "http": "iparchitect_39067_24_04_25:DD8nn2N9kQKrENY7QD@188.143.169.29:30568"
#
#     }
#
#     check_ip = requests.get(httpbin, proxies=proxy_1)
#     resp = check_ip.json()
#     pprint(resp)
#     # new_ip('188.143.169.29:30551')
#     # time.sleep(5)
#     # new_ip('188.143.169.29:30573')
#  'origin': '31.173.87.160',
#  'origin': '31.173.83.158',#  'origin': '178.176.72.94',


