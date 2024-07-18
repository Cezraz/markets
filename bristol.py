import json
import requests
import csv
def bristolDoCsv(search):
    page=1
    flag=False
    url = "https://api.mobile.bristol.ru/api/v3/products/search"

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'AnonToken': 'tVAss9VYmDPqnDUF/U+2vjVqgEBmXhQRQdbsEwdG8jOX9V+uW6kP03RfEPA5q3VFfqblJYN0YKR/R9bhSR82rg==',
        'BristolApiToken': 'token',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Origin': 'https://bristol.ru',
        'Pragma': 'no-cache',
        'Referer': 'https://bristol.ru/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'appversion': '1.0',
        'hash': '202d4c9e27cffffdb5329f47a4d96f8b',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'timestamp': '1721305874744',
    }

    params = {
        'consumer': 'website',
        'shop_number': 'f2585371-966a-11ee-b6df-00505684e1a4',
        'community_id': '17',
        'query': search,
        'page': page,
        'count': 100,
        'products_without_shop': 'false',
    }

    response = requests.get(url, headers=headers, params=params)
    #data = response.json()
    print(response)
#    while flag:
#        response = requests.get(url, headers=headers, params=params)
#        data = response.json()
#        if data['products_count'] <= page*100:
#            flag = False
#        for i in range(len(data['promo_products'])):
#            data_item = data['promo_products'][i]
#            data_price=""
#            match data_item['prices']['type']:
#                case "one_price":
#                    data_price = str(data_item['prices']['regular_price'])
#
#                case "show_where_to_buy_price_red_catalog" | "show_where_to_buy_price_yellow_catalog":
#                    data_price = str(data_item['prices']['show_where_to_buy_price'])
#
#                case _:
#                    data_price = str(data_item['prices']['promo_price'])
#
#            print(data_item['name'] + " : " + data_price)
#            if page == 1 and i == 0:
#                with open('bristol.csv', 'w+', newline='') as csvfile:
#                    writer = csv.writer(csvfile, delimiter=';',
#                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
#                    writer.writerow([data_item['name']] + [data_price])
#            else:
#                with open('bristol.csv', 'a+', newline='') as csvfile:
#                    writer = csv.writer(csvfile, delimiter=';',
#                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
#                    writer.writerow([data_item['name']] + [data_price])
#        page += 1


bristolDoCsv("пиво")