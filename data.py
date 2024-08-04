import json

import pyaterochka
from bristol import bristolDoCsv
from pyaterochka import pDoCsv
from magnit import magnitDoCsv
from maxi import maxiDoCsv
import yandex
import requests
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

def pyatDoCsv(search):
    flag = True
    offset = 0
    url_1 = "https://5d.5ka.ru/api/catalog/v2/stores/35QR/search?q=" + search + "&mode=store&offset=" + str(
        offset) + "&query_type=fuzzy&include_restrict=true&limit=200"
    url = "https://5d.5ka.ru/api/catalog/v2/stores/35QR/search"

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'dnt': '1',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }

    params = {
        'q': search,
        'mode': 'store',
        'offset': offset,
        'query_type': 'fuzzy',
        'include_restrict': 'true',
        'limit': 200,
    }

    while flag:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        # print(data['products'][0]['prices'])
        if data['products']:
            flag = False
        for i in range(len(data['products'])):

            if not data['products'][i]['promo']:
                true_price = data['products'][i]['prices']['regular']
            elif not data['products'][i]['prices']['regular'] and not data['products'][i]['prices']['cpd_promo_price']:
                true_price = data['products'][i]['prices']['discount']
            else:
                true_price = data['products'][i]['prices']['cpd_promo_price']

            if offset == 0 and i == 0:
                with open('5ka.csv', 'w+', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=';',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([str(data['products'][i]['name'])] + [true_price])
            else:
                with open('5ka.csv', 'a+', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=';',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([str(data['products'][i]['name'])] + [true_price])
            print(str(data['products'][i]['name']) + " " + str(true_price))
        offset += 200

def magnitDoCsv1(search):
    flag = True
    url = "https://magnit.ru/webgate/v2/goods/search"
    url_get = "https://magnit.ru/webgate/v1/promotions/search?storeCode=290053&query="+search+"&limit=36&offset=0"

    payload = {
        "includeForAdults": True,
        "term": search,
        "pagination": {"offset": 0,"limit": 36},
        "sort": {"order": "desc","type": "popularity"},
        "storeCode": "290053",
        "storeType": "1",
        "catalogType": "1"}
    headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '183',
    'Content-Type': 'application/json',
    'Dnt':'1',
    'Host':'magnit.ru',
    'Pragma': 'no-cache',
    'Referer': 'https://magnit.ru/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'X-App-Version': '7.0.0',
    'X-Client-Name': 'magnit',
    'X-Device-ID': '1084176D-1C26-E6AB-2B29-04D48306DC6D',
    'X-Device-Platform': 'Web',
    'X-Device-Tag': 'disabled',
    'X-New-Magnit': 'true',
    'X-Platform-Version': 'Windows Chrome 126',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    }
    headers_get = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Dnt':'1',
    'Host':'magnit.ru',
    'Pragma': 'no-cache',
    'Referer': 'https://magnit.ru/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'X-App-Version': '7.0.0',
    'X-Client-Name': 'magnit',
    'X-Device-ID': '1084176D-1C26-E6AB-2B29-04D48306DC6D',
    'X-Device-Platform': 'Web',
    'X-Device-Tag': 'disabled',
    'X-New-Magnit': 'true',
    'X-Platform-Version': 'Windows Chrome 126',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    }

    while flag:
        response = requests.post(url, headers=headers, json=payload)
        data = response.json()

        if data['pagination']['totalCount'] < (payload['pagination']['offset'] +payload['pagination']['limit']):
            flag = False
        for i in range(len(data['items'])):
            true_price = str(data['items'][i]['price'])[:-2] + ".99"
            if payload['pagination']['offset'] == 0 and i == 0:

                with open('magnit.csv', 'w+', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=';',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([str(data['items'][i]['name'])] + [true_price])
            else:
                with open('magnit.csv', 'a+', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=';',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([str(data['items'][i]['name'])] + [true_price])
            print(str(data['items'][i]['name']) + " " + true_price)
           # print("Обработано " + str(i + 1) + " страниц(a/ы) из " + str(len(data['items'])))
        payload['pagination']['offset'] += 36

    response = requests.get(url_get, headers=headers_get)
    data = response.json()
    for i in range(len(data['data'])):
        if "price" not in data['data'][i]:
            continue
        true_price = str(data['data'][i]['price'])[:-2] + ".99"
        with open('magnit.csv', 'a+', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([str(data['data'][i]['name'])] + [true_price])
        print(str(data['data'][i]['name']) + " " + true_price)

def maxiDoCsv1(search):
    #search ="adrenaline"
    driver = webdriver.Chrome()
    # загрузка страницы
    driver.get('https://maxi-retail.ru/arhangelsk/search?q='+search)

    # ожидание загрузки элемента
    elems=driver.find_elements(By.CLASS_NAME,"Paginate_link__2aPHY")
    total_pages = 1
    if elems:
        total_pages = int(elems[-1].text)
        print(total_pages)
    driver.close()

    for i in range(total_pages):
        response = requests.get("https://maxi-retail.ru/arhangelsk/search?offer=false&sort=POPULAR&q="+search+"&id=&page="+str(i))
        soup = BeautifulSoup(response.text,"html.parser")

        data_name = list(soup.find_all("span",class_="sc-bdvvtL fdJFhe Item_card__name__3q8_q"))
        names = []

        for item in data_name:
            temp_str = str(item).replace("/span>","")
            ind = temp_str.rfind(">")
            names.append(temp_str[ind+1:len(temp_str)-1])

        data_price = list(soup.find_all("span",class_="sc-bdvvtL eIXxjy"))
        prices = []

        for item in data_price:
            temp_str = str(item).replace("/span>","")
            ind = temp_str.rfind(">")
            prices.append(temp_str[ind+1:len(temp_str)-2])

        if i == 0:
            with open('maxi.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=';',
                                        quotechar ='|', quoting=csv.QUOTE_MINIMAL)
                for j in range(len(prices)):
                    writer.writerow([names[j]]+[prices[j]])
        else:
            with open('maxi.csv', 'a+', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=';',
                                        quotechar ='|', quoting=csv.QUOTE_MINIMAL)
                for j in range(len(prices)):
                    writer.writerow([names[j]]+[prices[j]])
        print("Обработано "+str(i+1)+" страниц(a/ы) из "+str(total_pages))


def getAllData(search):
    pDoCsv(search=search)
    magnitDoCsv(search=search)
    maxiDoCsv(search=search)
    bristolDoCsv(search=search)
    yandex.yandexDoCsv(search, "magnit_sem")
    yandex.yandexDoCsv(search, "lenta")

    market_files = ['5ka', 'magnit', 'maxi', 'bristol', 'yandex_magnit_sem', 'yandex_lenta']
    market_returns = {}
    remove_sumbols = "[']"

    for i in range(len(market_files)):
        rows = []
        with open("./" + market_files[i] + ".csv", 'r', encoding="utf-8") as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                str_row = str(row)
                for symbol in remove_sumbols:
                    str_row = str_row.replace(symbol, "")
                rows.append(str_row.split(";"))

        market_returns[market_files[i]] = rows
    return  market_returns


