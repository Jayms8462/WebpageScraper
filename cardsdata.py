from asyncio.windows_events import NULL
import csv
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from gtts import gTTS
import re

os.system('cls' if os.name == 'nt' else 'clear')
options = webdriver.FirefoxOptions()
# options.headless = True
driver = webdriver.Firefox(options = options)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}
url = [
    "https://www.tcgplayer.com/product/222877/weiss-schwarz-mob-psycho-100-100pct",
    "https://www.tcgplayer.com/product/24825/yugioh-dark-revelation-volume-2-7",
    "https://www.tcgplayer.com/product/23292/yugioh-ancient-sanctuary-7",
    "https://www.tcgplayer.com/product/122042/weiss-schwarz-love-live-dx-vol2-leftheartbeat",
    "https://www.tcgplayer.com/product/121994/weiss-schwarz-love-live-dx-vol2-leftheartbeat-eli-ayase",
    "https://www.tcgplayer.com/product/121995/weiss-schwarz-love-live-dx-vol2-leftheartbeat-nozomi-tojo"
]

column = ['Set Name', 'Card Name', 'Description', 'Image']
dataWorking = []

def findIndex(ele, arr):
    return arr.index(ele)

for url in url:
    output = []
    output = [''] * len(column)
    driver.get(url)
    #Grabs set name to filter out card name later

    try:
        time.sleep(2)
        setNameGroup = driver.find_element(By.CLASS_NAME, 'product-details__name').text

        setNameSplit = setNameGroup.split(' - ')
        card = setNameSplit[0]
        setName = setNameSplit[1]
    except:
        driver.refresh()
        time.sleep(4)
        setNameGroup = driver.find_element(By.CLASS_NAME, 'product-details__name').text

        setNameSplit = setNameGroup.split(' - ')
        card = setNameSplit[0]
        setName = setNameSplit[1]

    image = driver.find_element(By.CLASS_NAME, 'v-lazy-image.v-lazy-image-loaded').get_attribute('src')
        
    # Toggle for Read Me to grab all the data
    try:
        readMore = driver.find_element(By.CLASS_NAME, 'product__item-details__toggle.masked')
        readMore.click()
    except NoSuchElementException:
        readMore = ''

    # Grab Product Details
    try:
        description = driver.find_element(By.CLASS_NAME, 'product__item-details__description').text
    except:
        description = ''

    # Grab Product Attributes
    dataAttributes = driver.find_element(By.CLASS_NAME, 'product__item-details__attributes')
    pdList = dataAttributes.find_elements(By.TAG_NAME, 'li')

    # Splits Headers from Data
    columnHeaders = []
    columnClean = []
    data = []
    dataClean = []
    output = []
    for i in pdList:
        eleSplit = i.text.split(':')
        columnHeaders.append(eleSplit[0])
        data.append(eleSplit[1])

    for i in columnHeaders:
        str = i.split(' / ')
        for j in str:
            strSpl = j.split(' /')
            for k in strSpl:
                anoSpl = k.split('/ ')
                for l in anoSpl:
                    finSpl = l.split('/')
                    for m in finSpl:
                        columnClean.append(m)
                        if l not in column:
                            column.append(m)

    for i in data:
        str = i.split(' / ')
        for j in str:
            strSpl = j.split(' /')
            for k in strSpl:
                finalSpl = k.split('/ ')
                for l in finalSpl:
                    if l not in column:
                        dataClean.append(l)
    output = [''] * len(column)

    if len(columnClean) == len(dataClean):
        idxCount = 0
        # Sending page data out output array
        index = findIndex('Set Name', column)
        output[index] = setName

        index = findIndex('Card Name', column)
        output[index] = card

        index = findIndex('Description', column)
        output[index] = description

        index = findIndex('Image', column)
        output[index] = image

        for i in columnClean:
            indexNum = findIndex(i, column)
            output[indexNum] = dataClean[idxCount]
            idxCount += 1

        with open('test.csv', 'a', newline = "", encoding="utf-8") as f:
            write = csv.writer(f)
            write.writerows([output])
            f.close()

        print('Completed ', url)

    if len(columnClean) != len(dataClean):
        print('Hit issue with URL sending to issueUrl.txt: ' + url)
        with open('issueCards.txt', 'a') as f:
            f.write(url + '\n')
        f.close()

with open('test.csv', newline='') as f:
    data = csv.reader(f, delimiter=',')
    dataWorking.append(column)
    for i in data:
        dataWorking.append(i)
    f.close()

os.remove('test.csv')
with open('cardFinal.csv', 'a', newline = "", encoding="utf-8") as f:
    write = csv.writer(f)
    write.writerows(dataWorking)
    f.close()


# with open('test.csv', 'a', newline = "", encoding="utf-8") as f:
#     write = csv.writer(f)
#     write.writerows([column])
#     f.close()



# # now change the 2nd line, note that you have to add a newline
# data[1] = 'Mage\n'

# # and write everything back
# with open('stats.txt', 'w') as file:
#     file.writelines( data )