import json
import requests
import csv

def pDoCsv(search):
    offset = 0
    url_1 = "https://5d.5ka.ru/api/catalog/v2/stores/35QR/search?q="+search+"&mode=store&offset="+str(offset)+"&query_type=fuzzy&include_restrict=true&limit=200"
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

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    #print(data)
    if not data['products']:
        with open('5ka.csv', 'w+', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        print("Not found")
        return
    for i in range(len(data['products'])):

        if not data['products'][i]['promo']:
            true_price = data['products'][i]['prices']['regular']
        elif not data['products'][i]['prices']['regular'] and not data['products'][i]['prices']['cpd_promo_price']:
            true_price = data['products'][i]['prices']['discount']
        else:
            true_price = data['products'][i]['prices']['cpd_promo_price']

        if offset == 0 and i == 0:
            with open('5ka.csv', 'w+', newline='', encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile, delimiter=';',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([str(data['products'][i]['name'])] + [true_price])
        else:
            with open('5ka.csv', 'a+', newline='', encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile, delimiter=';',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([str(data['products'][i]['name'])] + [true_price])
        print(str(data['products'][i]['name']) + " " + str(true_price))

pDoCsv("Гриджо Каза Дефра")