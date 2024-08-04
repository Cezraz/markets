import json
import requests
import csv

def yandexDoCsv(search,place):
    api_place = ""
    match place:
        case "5ka":
            api_place = "pyaterochka_g9dvz"
        case "magnit":
            api_place = "magnit_celevaya_h4vbf"
        case "magnit_sem":
            api_place = "magnit_semejnyj_celevaya_5sntj"
        case "lenta":
            api_place = "lenta_vxtsi"
        case _:
            api_place = "magnit_celevaya_h4vbf"
            place="magnit"

    url = "https://eda.yandex.ru/api/v1/menu/search"

    cookies = {
        'i': '3qkrkAc4SOM+mNfRtYyUYbIdtUxT/UqxXuNydj5N2IXKFujMSkLNT27e+Zfp4eoDgPyhmUjkWAA5Q93xqgGmdNwZCA8=',
        'yandexuid': '959768691721201902',
        'yp': '1721814036.szm.1:1280x1024:1280x863',
        'is_gdpr': '0',
        'is_gdpr_b': 'CO6pNRD0hwI=',
        'yashr': '9097539661721209236',
        'receive-cookie-deprecation': '1',
        'bh': 'EkAiTm90L0EpQnJhbmQiO3Y9IjgiLCAiQ2hyb21pdW0iO3Y9IjEyNiIsICJHb29nbGUgQ2hyb21lIjt2PSIxMjYiKgI/MDoJIldpbmRvd3MiYJSj3rQG',
        'ys': 'c_chck.731178649',
        'PHPSESSID': '87bfc700f9014b0cb7863811fdbfbed9',
        '_yasc': '9pHotwxS7eneISgPeSAUPLhMouw/Vft8abwwSKuJ27oNvtfDsxP++hRRFxGttHwHPRZd',
        'eda_web': '{%22app%22:{%22analyticsSession%22:{%22id%22:%22lypom2it-ix6rhbwo5g-cfeov59itel-ulmup2wst8%22%2C%22start%22:1721211040%2C%22update%22:1721212456}%2C%22deliveryTime%22:null%2C%22themeVariantKey%22:%22light%22%2C%22xDeviceId%22:%22lypom2it-u0qe7cwft9-wxa5xvqol1-6mf94fxr8fb%22%2C%22lat%22:64.52620651492634%2C%22lon%22:40.60154645108283}}',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        # 'cookie': 'i=3qkrkAc4SOM+mNfRtYyUYbIdtUxT/UqxXuNydj5N2IXKFujMSkLNT27e+Zfp4eoDgPyhmUjkWAA5Q93xqgGmdNwZCA8=; yandexuid=959768691721201902; yp=1721814036.szm.1:1280x1024:1280x863; is_gdpr=0; is_gdpr_b=CO6pNRD0hwI=; yashr=9097539661721209236; receive-cookie-deprecation=1; bh=EkAiTm90L0EpQnJhbmQiO3Y9IjgiLCAiQ2hyb21pdW0iO3Y9IjEyNiIsICJHb29nbGUgQ2hyb21lIjt2PSIxMjYiKgI/MDoJIldpbmRvd3MiYJSj3rQG; ys=c_chck.731178649; PHPSESSID=87bfc700f9014b0cb7863811fdbfbed9; _yasc=Z9952QacDR1EZoL9guKxODd0Bm2Wmq+e+JcslZuw2ENCGl92Zw+4q0a6gB7rTgz6fbNu; eda_web={%22app%22:{%22analyticsSession%22:{%22id%22:%22lypom2it-ix6rhbwo5g-cfeov59itel-ulmup2wst8%22%2C%22start%22:1721211040%2C%22update%22:1721216504}%2C%22deliveryTime%22:null%2C%22themeVariantKey%22:%22light%22%2C%22xDeviceId%22:%22lypom2it-u0qe7cwft9-wxa5xvqol1-6mf94fxr8fb%22%2C%22lat%22:64.52620651492634%2C%22lon%22:40.60154645108283}}',
        'dnt': '1',
        'origin': 'https://eda.yandex.ru',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://eda.yandex.ru/retail/paterocka/search?placeSlug=pyaterochka_g9dvz&query=%D0%BC%D0%BE%D0%BB%D0%BE%D0%BA%D0%BE',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-app-version': '16.57.0',
        'x-client-session': 'lypom2it-ix6rhbwo5g-cfeov59itel-ulmup2wst8',
        'x-device-id': 'lypom2it-u0qe7cwft9-wxa5xvqol1-6mf94fxr8fb',
        'x-platform': 'desktop_web',
        'x-taxi': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 platform=eats_desktop_web',
        'x-ya-coordinates': 'latitude=64.52620651492634,longitude=40.60154645108283',
    }

    payload = {
        'region_id': 1,
        'place_slug': api_place,
        'text': search,
        'location': {
            'lat': 64.52620651492634,
            'lon': 40.60154645108283,
        },
    }
    response = requests.post(url, headers=headers, json=payload, cookies=cookies)
    data = response.json()
    if data['blocks'][0]['payload'] == {}:
        with open('yandex_' + place + '.csv', 'w+', newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=';',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        print("Not found")
        return
    for item in range(len(data['blocks'][0]['payload']['products'])):
        data_item = data['blocks'][0]['payload']['products'][item]
        print(str(data['blocks'][0]['payload']['products'][item]['name']))
        if '\xd7' in data_item['name']:
            data_item['name']=str(data_item['name']).replace('\xd7',"")
        if item == 0:
            with open('yandex_'+place+'.csv', 'w+', newline='', encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile, delimiter=';',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([data_item['name']] + [data_item['decimalPrice']])
        else:
            with open('yandex_'+place+'.csv', 'a+', newline='', encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile, delimiter=';',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([str(data_item['name'])] + [str(data_item['decimalPrice'])])
    print("done")

def yandexDoCsvAll(search):
    url = "https://eda.yandex.ru/eats/v1/full-text-search/v1/search"

    cookies = {
        'i': '1Awz/EK+xvzngjQmt0pd7zuT8Ox2dzAHt5QRL1wKVqPV2mhvhtUmz56iyb/SnyQRbOh7eErSkxUoFxUI6FkskD3RNz0=',
        'yandexuid': '8965804441721287884',
        'yashr': '2994075651721287884',
        'PHPSESSID': '0a2603fe4ced4ec5abdabcf10fa9c457',
        '_yasc': 'kZ2iwo/750/OGxqNG5ztvArkBrM616LPILamkBkt64Ya/c/vI4jRctkm/cT5uL2XxDDv',
        'eda_web_adult_confirmed': 'true',
        'eda_web': '{%22app%22:{%22analyticsSession%22:{%22id%22:%22lyqyd400-0z4fd9yv8nrj-8gow0fgdvac-4t4up1e5ceb%22%2C%22start%22:1721287885%2C%22update%22:1721292807}%2C%22deliveryTime%22:null%2C%22themeVariantKey%22:%22light%22%2C%22xDeviceId%22:%22lyqyd400-7qmwx87qwa2-08cqfddji57h-3je0uggpj8t%22%2C%22lat%22:64.52623809191257%2C%22lon%22:40.601306103235835}}',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        # 'cookie': 'i=1Awz/EK+xvzngjQmt0pd7zuT8Ox2dzAHt5QRL1wKVqPV2mhvhtUmz56iyb/SnyQRbOh7eErSkxUoFxUI6FkskD3RNz0=; yandexuid=8965804441721287884; yashr=2994075651721287884; PHPSESSID=0a2603fe4ced4ec5abdabcf10fa9c457; _yasc=kZ2iwo/750/OGxqNG5ztvArkBrM616LPILamkBkt64Ya/c/vI4jRctkm/cT5uL2XxDDv; eda_web_adult_confirmed=true; eda_web={%22app%22:{%22analyticsSession%22:{%22id%22:%22lyqyd400-0z4fd9yv8nrj-8gow0fgdvac-4t4up1e5ceb%22%2C%22start%22:1721287885%2C%22update%22:1721292807}%2C%22deliveryTime%22:null%2C%22themeVariantKey%22:%22light%22%2C%22xDeviceId%22:%22lyqyd400-7qmwx87qwa2-08cqfddji57h-3je0uggpj8t%22%2C%22lat%22:64.52623809191257%2C%22lon%22:40.601306103235835}}',
        'dnt': '1',
        'origin': 'https://eda.yandex.ru',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://eda.yandex.ru/search?query=adrenaline&type=shop',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-app-version': '16.57.0',
        'x-client-session': 'lyqyd400-0z4fd9yv8nrj-8gow0fgdvac-4t4up1e5ceb',
        'x-device-id': 'lyqyd400-7qmwx87qwa2-08cqfddji57h-3je0uggpj8t',
        'x-platform': 'desktop_web',
        'x-taxi': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 platform=eats_desktop_web',
        'x-ya-coordinates': 'latitude=64.52623809191257,longitude=40.601306103235835',
    }

    payload = {
        'text': 'adrenaline',
        'filters': [],
        'selector': 'shop',
        'location': {
            'longitude': 40.601306103235835,
            'latitude': 64.52623809191257,
        },
    }
    response = requests.post(url, headers=headers, json=payload, cookies=cookies)
    data = response.json()
    #print(data['blocks'][1]['payload'][0]['items'])
    for market in range(len(data['blocks'][1]['payload'])):
        for item in range(len(data['blocks'][1]['payload'][market]['items'])):
            data_item = data['blocks'][1]['payload'][market]['items'][item]
            #print(str(data_item['title']))
            if '\xd7' in data_item['title']:
               data_item['title']=str(data_item['title']).replace('\xd7',"")
            if item == 0:
               with open('yandex_all.csv', 'w+', newline='', encoding="utf-8") as csvfile:
                   writer = csv.writer(csvfile, delimiter=';',
                                       quotechar='|', quoting=csv.QUOTE_MINIMAL)
                   writer.writerow([data_item['title']] + [data_item['decimal_price']+".00"])
            else:
               with open('yandex_all.csv', 'a+', newline='', encoding="utf-8") as csvfile:
                   writer = csv.writer(csvfile, delimiter=';',
                                       quotechar='|', quoting=csv.QUOTE_MINIMAL)
                   writer.writerow([str(data_item['title'])] + [data_item['decimal_price']+".00"])
    print("done")

#yandexDoCsv("a231131231","lenta")