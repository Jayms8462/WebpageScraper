import csv
from subprocess import TimeoutExpired
import time
import os
from requests import Timeout
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

start_time = time.time()

os.system('cls' if os.name == 'nt' else 'clear')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}

urls = [
    
]

column = ['Set Name', 'Card Name', 'URL', 'Image', 'Description']

def issue(message, url):
    print(message + url)
    with open('issueCards.txt', 'a') as f:
        f.write(url + '\n')
    f.close()

def timeout(url):
    with open('timeoutCards.txt', 'a') as f:
        f.write(url + '\n')
    f.close()

def findIndex(ele, arr):
    return arr.index(ele)

def main(url):
    try:
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options = options)
        driver.set_page_load_timeout(10)
        driver.get(url)
        output = []
        try:
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "product-details__name")))
            except:
                driver.refresh()
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "product-details__name")))
            setNameGroup = driver.find_element(By.CLASS_NAME, 'product-details__name').text
            setNameSplit = setNameGroup.split(' - ')
            if setNameSplit == ['']:
                driver.refresh()
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "product-details__name")))
                setNameGroup = driver.find_element(By.CLASS_NAME, 'product-details__name').text
                setNameSplit = setNameGroup.split(' - ')
            if len(setNameSplit) != 2:
                driver.refresh()
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "product-details__name")))
                setNameGroup = driver.find_element(By.CLASS_NAME, 'product-details__name').text
                setNameSplit = setNameGroup.split(' - ')
        except:
            driver.close()
            options = webdriver.FirefoxOptions()
            options.headless = True
            driver = webdriver.Firefox(options = options)
            driver.get(url)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "product-details__name")))
            setNameGroup = driver.find_element(By.CLASS_NAME, 'product-details__name').text
            setNameSplit = setNameGroup.split(' - ')
        card = setNameSplit[1]
        setName = setNameSplit[0]
        image = driver.find_element(By.CLASS_NAME, 'progressive-image-main').get_attribute('src')
        try:
            readMore = driver.find_element(By.CLASS_NAME, 'product__item-details__toggle.masked')
            readMore.click()
        except:
            readMore = ''
        try:
            description = driver.find_element(By.CLASS_NAME, 'product__item-details__description').text
        except:
            description = ''
        
        dataAttributes = driver.find_element(By.CLASS_NAME, 'product__item-details__attributes')
        pdList = dataAttributes.find_elements(By.TAG_NAME, 'li')
        dataClean = []
        columnClean = []

        for i in pdList:
            attrib = i.text.split(':')
            if ' / ' in attrib[0]:
                attrib[0] = attrib[0].split(' / ')
            if ' /' in attrib[0]:
                attrib[0] = attrib[0].split(' /')
            if '/ ' in attrib[0]:
                attrib[0] = attrib[0].split('/ ')
            if '/' in attrib[0]:
                attrib[0] = attrib[0].split('/')

            if ' / / ' in attrib[1]:
                attrib[1] = attrib[1].split('/')
            if ' / /' in attrib[1]:
                attrib[1] = attrib[1].split(' /')
            if ' / ' in attrib[1]:
                attrib[1] = attrib[1].split(' / ')
            if ' /' in attrib[1]:
                attrib[1] = attrib[1].split(' /')
            if '/ ' in attrib[1]:
                attrib[1] = attrib[1].split('/ ')
            
            if type(attrib[0]) == str and type(attrib[1]) == str:
                columnClean.append(attrib[0])
                dataClean.append(attrib[1])
                if attrib[0] not in column:
                    column.append(attrib[0])
            if type(attrib[0]) == list and type(attrib[1]) == list:
                if len(attrib[0]) == len(attrib[1]):
                    for j in attrib[0]:
                        columnClean.append(j)
                        if j not in column:
                            column.append(j)
                    for j in attrib[1]:
                        dataClean.append(j)
                else:
                    raise ValueError('Issue with length on Attributes')
            if type(attrib[0]) == list and type(attrib[1]) == str:
                attrib[0] = '/'.join(attrib[0])
                columnClean.append(attrib[0])
                if attrib[0] not in column:
                    column.append(attrib[0])
                dataClean.append(attrib[1])
            
            if type(attrib[0]) == str and type(attrib[1]) == list or type(attrib[0]) == list and type(attrib[1]) == str:
                raise ValueError('Issue with length on Attributes')

        output = [''] * len(column)
        output[0] = setName
        output[1] = card
        output[2] = url
        output[3] = image
        output[4] = description
        
        for i, x in enumerate(columnClean):
            output[findIndex(x, column)] = dataClean[i]

        with open('cardColumns.csv', 'w', newline = "", encoding="utf-8") as f:
            write = csv.writer(f)
            write.writerows([column])
            f.close()

        with open('test.csv', 'a', newline = "", encoding="utf-8") as f:
            write = csv.writer(f)
            write.writerows([output])
            f.close()
        print('Completed:', url)
    except TimeoutException:
        print('Hit TimeoutException with:', url)
        driver.close()
        # timeout(url)
        main(url)
    except Exception as e:
        issue('Issue with book, sending to issueCard.txt:', url)

for url in urls:
    main(url)