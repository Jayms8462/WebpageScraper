import csv
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from gtts import gTTS
import re

os.system('cls' if os.name == 'nt' else 'clear')

driver = webdriver.Firefox()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}
url = [

]

for url in url:
    output = []
    driver.get(url)
    data = driver.find_elements(By.CLASS_NAME, 'productDetail')
    for i in data:
        text = i.text
        link = driver.find_element(By.LINK_TEXT, i.text).get_attribute('href')
        output.append([text, link])

    with open('card.csv', 'a', encoding="utf-8") as f:
        write = csv.writer(f)
        write.writerows(output)
    f.close()
    print('Completed ' + url)

driver.close()