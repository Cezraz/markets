import undetected_chromedriver as uc
import time

driver = uc.Chrome()
driver.get('https://bristol.ru/search?s=%D0%BF%D0%B8%D0%B2%D0%BE')
time.sleep(5)
cookies=driver.get_cookies()
res={}
print(cookies)
for item in range(len(cookies)):
    res[cookies[item]['name']] = cookies[item]['value']
print(res)

#print(driver.get_downloadable_files())
#driver.save_screenshot('nowsecure.png')