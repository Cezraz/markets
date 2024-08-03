import json
import requests
import csv
import time
import re

import undetected_chromedriver as uc
import time
def bristolDoCsv(search):
    driver = uc.Chrome()
    driver.get('https://bristol.ru/search?s='+search)
    time.sleep(2)
    cookies = driver.get_cookies()
    res = {}
    #print(cookies)
    for item in range(len(cookies)):
        res[cookies[item]['name']] = cookies[item]['value']
    #print(res)
    driver.close()

    page = 1
    flag = True
    url = "https://api.mobile.bristol.ru/api/v3/products/search"
    t = str(int(time.time()//1))



    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'AnonToken': 'QekYdJM5QmvFblVTFHJFO9Em24XhaQeh5ATKlKjHb6qL9trbcIS9r6PPT3yy2dB1du/JX3VDIk1RRHCocks+cQ==',
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
    'hash': '808fe063485d69252c9ba21ed1fd3802',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'timestamp': t,
    }

    params = {
        'consumer': 'website',
        'shop_number': 'f2585371-966a-11ee-b6df-00505684e1a4',
        'community_id': '17',
        'query': search,
        'page': page,
        'count': 24,
        'products_without_shop': 'false',
        'sort': 'popularity_first',
    }

    #page=2
    #response = requests.get(url, headers=headers, params=params, cookies=res)
    #data = response.json()
    #data_item = data['promo_products'][0]
    #print(data)

    while flag:
        params = {
            'consumer': 'website',
            'shop_number': 'f2585371-966a-11ee-b6df-00505684e1a4',
            'community_id': '17',
            'query': search,
            'page': page,
            'count': 24,
            'products_without_shop': 'false',
            'sort': 'popularity_first',
        }
        response = requests.get(url, headers=headers, params=params, cookies=res)
        data = response.json()
        #print(data)
        if data['products_count'] == 0:
            with open('bristol.csv', 'w+', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=';',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            print("Not found")
            flag=False
            break
        if data['products_count'] <= page*24:
            flag = False
        for i in range(len(data['promo_products'])):
            data_item = data['promo_products'][i]
            data_price=""
            if data_item['prices'] is None:
                #print(data_item)
                continue
            match data_item['prices']['type']:
                case "one_price":
                    data_price = str(data_item['prices']['regular_price'])

                case "show_where_to_buy_price_red_catalog" | "show_where_to_buy_price_yellow_catalog" | "show_where_to_buy_price_white_catalog" :
                    data_price = str(data_item['prices']['show_where_to_buy_price'])

                case _:
                    #print(data_item['prices']['type'])
                    data_price = str(data_item['prices']['promo_price'])

            #print(data_item['name'] + " : " + data_price)

            if page == 1 and i == 0:
                with open('bristol.csv', 'w+', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=';',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data_item['name']] + [data_price])
            else:
                with open('bristol.csv', 'a+', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=';',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data_item['name']] + [data_price])
        page += 1


#bristolDoCsv("321312412412413412")