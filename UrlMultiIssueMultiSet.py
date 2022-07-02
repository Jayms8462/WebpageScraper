# from asyncio.windows_events import NULL
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


fields = [['Title', 'Volume', 'Publisher', 'Label', 'Issue Number', 'Image','Cover Date', 'Cover Price', 'ISBN/UPC', 'Contributors', 'Characters', 'Details', 'URL'],[]]
startTime = time.time()
driver = webdriver.Firefox()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}
url = [

]

os.system('cls' if os.name == 'nt' else 'clear')

for urls in url:
    multiPage = False
    sets = 0
    errCounter = 0
    driver.get(urls)
    time.sleep(3)

    ## Get Sets
    pageSetTables = driver.find_elements(By.XPATH, '/html/body/div[6]/div[1]/div[2]/div/form/div/table/tbody/tr')
    for i in pageSetTables:
        match i.get_attribute('class'):
            case 'type_footer type_footer_1':
                multiPage = True
            case _:
                sets += 1
        del i
    del pageSetTables
    
    ## Gets Issues
    links = []

    def getIssues(counter, errCounter):
        workingArea = []
        issueNums = driver.find_elements(By.CLASS_NAME, 'issue')
        for i in issueNums:
            match i.text:
                case '': dump = i.text; del dump
                case ' Issues': dump = i.text; del dump
                case ' Annuals': dump = i.text; del dump
                case ' Giant Sizes': dump = i.text; del dump
                case ' King Sizes': dump = i.text; del dump
                case ' Specials': dump = i.text; del dump
                case ' Hard Covers': dump = i.text; del dump
                case ' Soft Covers': dump = i.text; del dump
                case ' TPBs': dump = i.text; del dump
                case _:
                    workingArea.append(i.text.strip())
            del i
        del issueNums

        if not workingArea:
            pageList = driver.find_elements(By.CLASS_NAME, 'g')
            print('Hit Empty Arr')
            try:
                pageList[counter].click()
                getIssues(counter, errCounter)
            except:
                errCounter = errCounter + 1
                if errCounter < 3:
                    getIssues(counter, errCounter)
                else:
                    print('Hit issue with URL sending to issueUrl.txt: ' + urls)
                    with open('issueUrl.txt', 'a') as f:
                        f.write(urls + '\n')
                    f.close()
        
        for i in workingArea:
            with open('issueLinks.txt', 'a') as f:
                f.write(driver.find_element(By.PARTIAL_LINK_TEXT, i).get_attribute('href') + '\n')
            f.close()
            del i

    if multiPage == True:
        counter = 0
        pageList = driver.find_element(By.CLASS_NAME, 'n')
        if pageList.get_attribute('style') == 'display: none;':
            for i in driver.find_elements(By.CLASS_NAME, 'g'):
                i.click()
                time.sleep(3)
                getIssues(counter, errCounter)
                counter += 1
            del i
        if pageList.get_attribute('style') == '':
            pageList = driver.find_element(By.CLASS_NAME, 'n')
            time.sleep(3)
            getIssues(counter, errCounter)
            for i in driver.find_elements(By.CLASS_NAME, 'g'):
                pageList.click()
                time.sleep(3)
                getIssues(counter, errCounter)
                counter += 1
            del i
        del pageList
    else:
        counter = 0
        getIssues(counter, errCounter)

    if sets > 1:
        counter = 0
        setsExpand = driver.find_elements(By.CLASS_NAME, 'expand')
        for i in setsExpand:
            time.sleep(3)
            i.click()
            getIssues(counter, errCounter)
            del i
        del setsExpand
    
    print("--- %s seconds ---" % (time.time() - startTime))
    print("Url Completed:", urls)