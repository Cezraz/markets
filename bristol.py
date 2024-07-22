import json
import requests
import csv
import time
import re

import undetected_chromedriver as uc
import time
def bristolDoCsv(search):
    driver = uc.Chrome()
    driver.get('https://bristol.ru/search?s=%D0%BF%D0%B8%D0%B2%D0%BE')
    time.sleep(2)
    cookies = driver.get_cookies()
    res = {}
    #print(cookies)
    for item in range(len(cookies)):
        res[cookies[item]['name']] = cookies[item]['value']
    #print(res)

    page=1
    flag=True
    token_url="https://bristol.ru/search?s=%D0%BF%D0%B8%D0%B2%D0%BE"
    url = "https://api.mobile.bristol.ru/api/v3/products/search"
    t = str(int(time.time()//1))
    t_float=str(time.time().__round__(3))


    token_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'bristol_local_anonymous=3R0Z2ClJJydb%2BX1s4ARamSmiunXpD%2BWaAYyx0SyMq%2F5mNlZdu5xFP2Dcsa7DTmJz0Apybqh4N5jVTyLNJ0XF%2FA%3D%3D; _userGUID=0:lys9b7xs:CoigBv0SNlUrUrP~2_RZ30wj4eru9k69; qrator_ssid=1721371260.609.3ecMl4HiRHxaq2l7-sivpqlnf7655t5rl8v1ijj3kt8d6878u; dSesn=71676992-0d85-778f-40cd-f989705f58a2; _dvs=0:lysc08h6:mQdnUGFPxrU8PPJA5Tll4KDOocHdFjiM; qrator_jsid=1721371261.996.3KbrqhvO1wXiHbxo-j9qh4muag8tel8jgpb3hl7l6cgmc5v62',
    'DNT': '1',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    }

    token_params = {
        's': 'пиво',
    }

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
        'count': 100,
        'products_without_shop': 'false',
    }

    session = requests.session()
    token_response = session.get(token_url,headers=token_headers,params=token_params,cookies=res)
    res_cook = token_response.cookies
    response = session.get(url, headers=headers, params=params, cookies=res_cook)
    #print(response.json())

    while flag:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        if data['products_count'] <= page*100:
            flag = False
        for i in range(len(data['promo_products'])):
            data_item = data['promo_products'][i]
            data_price=""
            match data_item['prices']['type']:
                case "one_price":
                    data_price = str(data_item['prices']['regular_price'])

                case "show_where_to_buy_price_red_catalog" | "show_where_to_buy_price_yellow_catalog":
                    data_price = str(data_item['prices']['show_where_to_buy_price'])

                case _:
                    data_price = str(data_item['prices']['promo_price'])

            print(data_item['name'] + " : " + data_price)
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


bristolDoCsv("пиво")