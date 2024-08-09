import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Загрузка куков из файла
with open('cookies.json', 'r') as file:
    cookies_list = json.load(file)

# Настройки Selenium
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL для запроса
url = 'https://pro.avito.ru/statistics'

# Открываем страницу
driver.get(url)

# Устанавливаем куки
for cookie in cookies_list:
    cookie_dict = {
        'name': cookie['name'],
        'value': cookie['value'],
        'domain': cookie['domain'],
        'path': cookie['path'],
        'secure': cookie['secure'],
        'httpOnly': cookie['httpOnly'],
    }
    if 'expirationDate' in cookie:
        cookie_dict['expiry'] = int(cookie['expirationDate'])
    driver.add_cookie(cookie_dict)

# Перезагружаем страницу с установленными куки
driver.get(url)
time.sleep(5)  # Ждем загрузки страницы

# Получаем HTML страницы
html = driver.page_source

# Закрываем драйвер
driver.quit()

# Создаем объект BeautifulSoup для парсинга HTML
soup = BeautifulSoup(html, 'html.parser')

# Ищем элемент h3 с нужными классами
titles = soup.find('h3', class_='styles-module-root-DMJPn styles-module-root-ZXV3x styles-module-size_xl-VXlBo styles-module-size_xl_dense-o6oau styles-module-size_xl-Aa8Ae styles-module-size_dense-CoFzr stylesMarginDense-module-root-VEwa5 stylesMarginDense-module-header-xl-R4QFp styles-module-root_top-yS5t5 styles-module-margin-top_4-o6CRC')

# Печатаем все найденные названия товаров
for title in titles:
    print(title.text)



# Ищем элементы с другой разметкой
other_elements = soup.find_all('span', class_='styles-module-wrapper-oT74B')

coun = 0
# Печатаем содержимое других элементов
for element in other_elements:
    coun+= 1
    if coun != 4:
        pass
    else:
        print(element.text)




# Ищем элементы с другой разметкой
other_elements1 = soup.find_all('p', class_='styles-module-root-ZXV3x styles-module-size_ms-fh7oj styles-module-size_ms_dense-qE7e9 styles-module-size_ms-OZwRo styles-module-textAlign_end-Q9dH6 styles-module-size_dense-CoFzr undefined stylesMarginDense-module-root-VEwa5')

count = 0
# Печатаем содержимое других элементов
for element1 in other_elements1:
    if count in [4, 5]:  # Индексы 5 и 6 по факту будут 4 и 5 в нулевой индексации
        print(element1.text)
    count += 1
