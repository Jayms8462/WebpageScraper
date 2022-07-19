import csv
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

start_time = time.time()

os.system('cls' if os.name == 'nt' else 'clear')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'}

urls = [
    "https://www.tcgplayer.com/product/57795/yugioh-yu-gi-oh-5ds-tag-force-promotional-cards-liberty-at-last",
    "https://www.tcgplayer.com/product/59234/yugioh-battle-pack-epic-dawn-liberty-at-last",
    "https://www.tcgplayer.com/product/69761/yugioh-battle-pack-epic-dawn-liberty-at-last-starfoil",
    "https://www.tcgplayer.com/product/115834/yugioh-premium-gold-infinite-gold-libic-malebranche-of-the-burning-abyss",
    "https://www.tcgplayer.com/product/95484/yugioh-secrets-of-eternity-libic-malebranche-of-the-burning-abyss",
    "https://www.tcgplayer.com/product/211522/cardfight-vanguard-v-eb13-the-astral-force-libitina-of-burial-rites",
    "https://www.tcgplayer.com/product/205150/universus-soulcalibur-vi-libra-of-souls-libra-of-souls",
    "https://www.tcgplayer.com/product/123886/future-card-buddyfight-annihilate-great-demonic-dragon-libra-starsentinel-leebra",
    "https://www.tcgplayer.com/product/259934/wixoss-glowing-diva-libra-natural-planet-queen",
    "https://www.tcgplayer.com/product/35288/wow-wrathgate-libram-of-radiance",
    "https://www.tcgplayer.com/product/250124/exodus-tcg-threshold-of-time-librarian-license",
    "https://www.tcgplayer.com/product/215687/magic-core-set-2021-library-larcenist",
    "https://www.tcgplayer.com/product/250123/exodus-tcg-threshold-of-time-library-litigation",
    "https://www.tcgplayer.com/product/70741/cardfight-vanguard-eb-dazzling-divas-library-madonna-rion",
    "https://www.tcgplayer.com/product/3215/magic-arabian-nights-library-of-alexandria",
    "https://www.tcgplayer.com/product/21516/magic-oversize-cards-library-of-alexandria-oversized",
    "https://www.tcgplayer.com/product/2635/magic-classic-sixth-edition-library-of-lat-nam",
    "https://www.tcgplayer.com/product/4186/magic-alliances-library-of-lat-nam",
    "https://www.tcgplayer.com/product/109163/magic-fourth-edition-foreign-white-border-library-of-leng",
    "https://www.tcgplayer.com/product/109541/magic-fourth-edition-foreign-black-border-library-of-leng",
    "https://www.tcgplayer.com/product/109859/magic-revised-edition-foreign-black-border-library-of-leng",
    "https://www.tcgplayer.com/product/110165/magic-revised-edition-foreign-white-border-library-of-leng",
    "https://www.tcgplayer.com/product/1169/magic-alpha-edition-library-of-leng",
    "https://www.tcgplayer.com/product/1475/magic-revised-edition-library-of-leng",
    "https://www.tcgplayer.com/product/1821/magic-fourth-edition-library-of-leng",
    "https://www.tcgplayer.com/product/211710/magic-summer-magic-library-of-leng",
    "https://www.tcgplayer.com/product/2253/magic-fifth-edition-library-of-leng",
    "https://www.tcgplayer.com/product/8814/magic-beta-edition-library-of-leng",
    "https://www.tcgplayer.com/product/9116/magic-unlimited-edition-library-of-leng",
    "https://www.tcgplayer.com/product/97534/magic-collectors-edition-library-of-leng-ce",
    "https://www.tcgplayer.com/product/97232/magic-international-edition-library-of-leng-ie",
    "https://www.tcgplayer.com/product/186489/final-fantasy-tcg-opus-viii-libroarian",
    "https://www.tcgplayer.com/product/262354/yugioh-battle-of-chaos-libromancer-agent",
    "https://www.tcgplayer.com/product/271810/yugioh-dimension-force-libromancer-bonded",
    "https://www.tcgplayer.com/product/271811/yugioh-dimension-force-libromancer-displaced",
    "https://www.tcgplayer.com/product/262356/yugioh-battle-of-chaos-libromancer-doombroker",
    "https://www.tcgplayer.com/product/271611/yugioh-dimension-force-libromancer-fire",
    "https://www.tcgplayer.com/product/271808/yugioh-dimension-force-libromancer-fireburst",
    "https://www.tcgplayer.com/product/262355/yugioh-battle-of-chaos-libromancer-firestarter",
    "https://www.tcgplayer.com/product/262357/yugioh-battle-of-chaos-libromancer-first-appearance",
    "https://www.tcgplayer.com/product/262248/yugioh-battle-of-chaos-libromancer-geek-boy",
    "https://www.tcgplayer.com/product/265398/yugioh-battle-of-chaos-libromancer-geek-boy-premier-edition",
    "https://www.tcgplayer.com/product/262358/yugioh-battle-of-chaos-libromancer-intervention",
    "https://www.tcgplayer.com/product/262353/yugioh-battle-of-chaos-libromancer-magigirl",
    "https://www.tcgplayer.com/product/271807/yugioh-dimension-force-libromancer-mystigirl",
    "https://www.tcgplayer.com/product/271812/yugioh-dimension-force-libromancer-prevented",
    "https://www.tcgplayer.com/product/271809/yugioh-dimension-force-libromancer-realized",
    "https://www.tcgplayer.com/product/208912/star-wars-destiny-covert-missions-licensed-to-fly",
    "https://www.tcgplayer.com/product/1170/magic-alpha-edition-lich",
    "https://www.tcgplayer.com/product/153383/final-fantasy-tcg-opus-iv-lich",
    "https://www.tcgplayer.com/product/211274/final-fantasy-tcg-opus-xi-lich",
    "https://www.tcgplayer.com/product/8815/magic-beta-edition-lich",
    "https://www.tcgplayer.com/product/9117/magic-unlimited-edition-lich",
    "https://www.tcgplayer.com/product/115065/dice-masters-dandd-faerun-under-siege-lich-greater-undead",
    "https://www.tcgplayer.com/product/115064/dice-masters-dandd-faerun-under-siege-lich-lesser-undead",
    "https://www.tcgplayer.com/product/115066/dice-masters-dandd-faerun-under-siege-lich-paragon-undead",
    "https://www.tcgplayer.com/product/97535/magic-collectors-edition-lich-ce",
    "https://www.tcgplayer.com/product/97233/magic-international-edition-lich-ie",
    "https://www.tcgplayer.com/product/245319/final-fantasy-tcg-opus-xiv-crystal-abyss-lich-ix",
    "https://www.tcgplayer.com/product/175145/force-of-will-valhalla-cluster-starter-deck-lich-lich-the-saint-of-death",
    "https://www.tcgplayer.com/product/183109/force-of-will-promo-cards-lich-lich-the-saint-of-death",
    "https://www.tcgplayer.com/product/248680/magic-the-list-lich-lord-of-unx",
    "https://www.tcgplayer.com/product/31762/magic-alara-reborn-lich-lord-of-unx",
    "https://www.tcgplayer.com/product/165468/yugioh-structure-deck-lair-of-darkness-lich-lord-king-of-the-underworld",
    "https://www.tcgplayer.com/product/25788/yugioh-force-of-the-breaker-lich-lord-king-of-the-underworld",
    "https://www.tcgplayer.com/product/47572/yugioh-gold-series-4-pyramids-edition-lich-lord-king-of-the-underworld",
    "https://www.tcgplayer.com/product/141850/weiss-schwarz-konosuba-lich-wiz",
    "https://www.tcgplayer.com/product/141851/weiss-schwarz-konosuba-lich-wiz-rrr",
    "https://www.tcgplayer.com/product/272340/force-of-will-game-of-gods-revolution-lich-immortal-saint",
    "https://www.tcgplayer.com/product/272341/force-of-will-game-of-gods-revolution-lich-immortal-saint-full-art",
    "https://www.tcgplayer.com/product/197343/force-of-will-the-decisive-battle-of-valhalla-lich-the-resurrected-cleric",
    "https://www.tcgplayer.com/product/197414/force-of-will-the-decisive-battle-of-valhalla-lich-the-resurrected-cleric-full-art",
    "https://www.tcgplayer.com/product/5878/magic-visions-lichenthrope",
    "https://www.tcgplayer.com/product/168462/magic-core-set-2019-lichs-caress",
    "https://www.tcgplayer.com/product/162171/magic-dominaria-lichs-mastery",
    "https://www.tcgplayer.com/product/165569/magic-prerelease-cards-lichs-mastery",
    "https://www.tcgplayer.com/product/210381/magic-mystery-booster-retail-exclusives-lichs-mirror",
    "https://www.tcgplayer.com/product/27721/magic-shards-of-alara-lichs-mirror",
    "https://www.tcgplayer.com/product/11639/magic-darksteel-lichs-tomb",
    "https://www.tcgplayer.com/product/162475/future-card-buddyfight-new-world-chaos-licht-sd-and-dunkelheit-sd",
    "https://www.tcgplayer.com/product/139818/magic-commander-2017-licia-sanguine-tribune",
    "https://www.tcgplayer.com/product/157720/pokemon-sm-ultra-prism-lickilicky",
    "https://www.tcgplayer.com/product/189255/pokemon-sm-unbroken-bonds-lickilicky",
    "https://www.tcgplayer.com/product/195162/pokemon-sm-unified-minds-lickilicky"
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
    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(options = options)
    driver.set_page_load_timeout(10)
    driver.get(url)
    try:
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
        driver.close()
        print('Completed:', url)
    except TimeoutException:
        print('Hit TimeoutException with:', url)
        driver.close()
        main(url)
        # timeout(url)
    except Exception as e:
        issue('Issue with book, sending to issueCard.txt:', url)
        driver.close()

for url in urls:
    main(url)