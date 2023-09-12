import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from seleniumwire import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
ip = 'любой ip' 


#Прокси лучше использовать свой
options = {'proxy': {
    'https': f'https://cCH6pB:LNteL9@{ip}',
    }}
# Инициализация веб-драйвера
#with webdriver.Chrome() as browser:
#    wait = WebDriverWait(browser, 50)
#    browser.get('https://sbermegamarket.ru/catalog/igrovye-pristavki-playstation/')
#    time.sleep(70)
#    list_sp = []
#    res = []
#
#    while True:
#        # Поиск всех элементов
#        items = browser.find_elements(By.XPATH, "//div[@class='item-title']/a")
#
#        for x in items:
#            if x.text not in list_sp:
#                res.append(x.text)
#                list_sp.append(x.text)
#
#        # Проверка наличия кнопки "Товары не в наличии"
#        if EC.presence_of_element_located((By.CLASS_NAME, 'catalog-listing__out-of-stock_heading')):
#            flag = False
#
#        # Случайная задержка перед скроллингом
#        delay = random.uniform(1, 3)
#        time.sleep(delay)
#
#        # Попытка скроллинга
#        try:
#            div = browser.find_element(By.XPATH, "//button[@class='btn-cloudy xl catalog-listing__show-more']")
#            browser.execute_script("arguments[0].scrollIntoView();", div)
#            wait.until(EC.staleness_of(div))
#        except:
#            break
#
#        # Случайная задержка перед следующим запросом
#        delay = random.uniform(2, 5)
#        time.sleep(delay)
#
#print(res)

with webdriver.Chrome(seleniumwire_options=options) as browser:
    browser.get('https://sbermegamarket.ru/catalog/igrovye-pristavki-playstation/')
    time.sleep(30)
    list_sp = []
    res = []
    div = browser.find_element(By.XPATH, "//button[@class='btn-cloudy xl catalog-listing__show-more']")
    time.sleep(2)
    flag = True
    while flag:
        #Скроллинг
        ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()
        time.sleep(10)
        for x in browser.find_elements(By.XPATH, "//div[@class='item-title']/a"):
            if x not in list_sp:
                res.append(x.text)
                if browser.find_element(By.CLASS_NAME, 'catalog-listing__out-of-stock_heading').text == 'Товары не в наличии':
                    flag = False
                list_sp.append(x)
print(res)
