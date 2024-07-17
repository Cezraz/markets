import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def maxiDoCsv(search):
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

