# from asyncio.windows_events import NULL
import csv
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from gtts import gTTS
import re

os.system('cls' if os.name == 'nt' else 'clear')

# driver = webdriver.Firefox()
options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(options = options)

def problem():
    tts = gTTS(text="Page did not load", lang='en')
    tts.save("loadIssue.mp3")
    os.system("start loadIssue.mp3")

    time.sleep(2)
    os.system("TASKKILL /F /IM vlc.exe")

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}
url = [

]

pages = []
titles = []
sets = []
links = []
contribData = []
charData = []
fields = [['Title', 'Volume', 'Publisher', 'Label', 'Issue Number', 'Image','Cover Date', 'Cover Price', 'ISBN/UPC', 'Contributors', 'Characters', 'Details', 'URL'],[]]

with open('Example.csv', 'w', encoding="utf-8") as f:
    write = csv.writer(f)
    write.writerows(fields)
f.close()

def clear(array, string):
    workingArr = []
    outputStr = ''
    for i in array:
        if i.text != string:
            workingArr.append(i.text)
        else: workingArr = ''
    if workingArr != '':
        outputStr = '\n'.join(workingArr)
    return outputStr

def getDataSingle(counter):
        try:
            output = []
            title = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[2]/div/ul/li[2]/h2').text
            volume = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[2]/div/div[2]').text
            publisher = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[2]/div/div[2]/a').text
            split_string = volume.split(' ' + publisher, 1)
            volume = split_string[0]
            label = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[2]/div/div[4]/div/div[1]/div[1]/table/tbody/tr[1]/td[1]').text
            issueNum = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[2]/div/div[4]/div/div[1]/div[1]/table/tbody/tr[1]/td[2]').text
            try:
                image = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[2]/div/div[4]/div/div[1]/div[1]/table/tbody/tr[1]/td[3]/a').get_attribute('href')
            except:
                image = ''
            coverDate = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[2]/div/div[4]/div/div[1]/div[1]/table/tbody/tr[2]/td[2]').text
            coverPrice = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[2]/div/div[4]/div/div[1]/div[1]/table/tbody/tr[3]/td[2]').text
            isbn = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[2]/div/div[4]/div/div[1]/div[1]/table/tbody/tr[9]/td[2]').text
            details = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[2]/div/div[4]/div/div[2]/div[1]').text

            contribData = []
            contrib = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[2]/div/div[4]/div/ul[2]/li[3]/a/em')
            contrib.click()
            contribDataEle = driver.find_elements(By.XPATH, '/html/body/div[6]/div[1]/div[2]/div/div[4]/div/div[2]/div[2]/ul/li')
            contribData = clear(contribDataEle, 'There have been no contributors assigned to this issue')
            
            charData = []
            characters = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[2]/div/div[4]/div/ul[2]/li[4]/a/em')
            characters.click()
            charDataEle = driver.find_elements(By.XPATH, '/html/body/div[6]/div[1]/div[2]/div/div[4]/div/div[2]/div[3]/ul/li')
            charData = clear(charDataEle, 'There have been no characters assigned to this issue')

            output.append([title, volume, publisher, label, issueNum, image, coverDate, coverPrice, isbn, contribData, charData, details, url])

            with open('Example.csv', 'a', newline = "", encoding="utf-8") as f:
                write = csv.writer(f)
                write.writerows(output)
            f.close()
            print('Completed ' + url)
        except:
            counter = counter + 1
            if counter < 3:
                print(counter)
                print('Hit Except on ' + url)
                print('Trying the URL again')
                time.sleep(5)
                getDataSingle(counter)
            else:
                print('Hit issue with URL sending to issueUrl.txt: ' + url)
                with open('issueUrl.txt', 'a') as f:
                    f.write(url + '\n')
                f.close()


for url in url:
    driver.get(url)
    time.sleep(2)
    counter = 0
    getDataSingle(counter)