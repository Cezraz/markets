import json
import requests
import csv

def magnitDoCsv(search):
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




