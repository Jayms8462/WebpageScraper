import csv
from socket import timeout
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import imageDownload as imgD

start_time = time.time()

os.system('cls' if os.name == 'nt' else 'clear')
options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(options = options)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}
url = [
    "https://www.tcgplayer.com/product/222877/weiss-schwarz-mob-psycho-100-100pct",
    "https://www.tcgplayer.com/product/23292/yugioh-ancient-sanctuary-7",
    "https://www.tcgplayer.com/product/24825/yugioh-dark-revelation-volume-2-7",
    "https://www.tcgplayer.com/product/122042/weiss-schwarz-love-live-dx-vol2-leftheartbeat",
    "https://www.tcgplayer.com/product/121994/weiss-schwarz-love-live-dx-vol2-leftheartbeat-eli-ayase",
    "https://www.tcgplayer.com/product/121995/weiss-schwarz-love-live-dx-vol2-leftheartbeat-nozomi-tojo",
    "https://www.tcgplayer.com/product/221869/weiss-schwarz-mob-psycho-100-lol-cult-member",
    "https://www.tcgplayer.com/product/221870/weiss-schwarz-mob-psycho-100-lol-mask",
    "https://www.tcgplayer.com/product/252347/metazoo-nightfall-first-edition-nameless-token",
    "https://www.tcgplayer.com/product/115571/weiss-schwarz-the-idolmster-cinderella-girls-asterisk-miku",
    "https://www.tcgplayer.com/product/115610/weiss-schwarz-the-idolmster-cinderella-girls-asterisk-riina",
    "https://www.tcgplayer.com/product/115611/weiss-schwarz-the-idolmster-cinderella-girls-asterisk-riina-sr",
    "https://www.tcgplayer.com/product/200383/weiss-schwarz-bang-dream-girls-band-party-vol2-h-hello-rinko-shirokane",
    "https://www.tcgplayer.com/product/200781/weiss-schwarz-bang-dream-girls-band-party-vol2-h-hello-rinko-shirokane-spm-a",
    "https://www.tcgplayer.com/product/200782/weiss-schwarz-bang-dream-girls-band-party-vol2-h-hello-rinko-shirokane-spm-b",
    "https://www.tcgplayer.com/product/200780/weiss-schwarz-bang-dream-girls-band-party-vol2-h-hello-rinko-shirokane-sr",
    "https://www.tcgplayer.com/product/114540/future-card-buddyfight-neo-enforcer-vere-or-so-the-dream-i-had-went",
    "https://www.tcgplayer.com/product/213499/future-card-buddyfight-buddy-again-vol2-~super-buddy-war-ex~-or-so-the-dream-i-had-went",
    "https://www.tcgplayer.com/product/259283/wixoss-diva-debut-deck-d02-nijisanji-ver-sanbaka-assist-ange-level-1",
    "https://www.tcgplayer.com/product/259359/wixoss-interlude-diva-assist-ange-level-1",
    "https://www.tcgplayer.com/product/259482/wixoss-interlude-diva-assist-ange-level-1-parallel-foil",
    "https://www.tcgplayer.com/product/259285/wixoss-diva-debut-deck-d02-nijisanji-ver-sanbaka-assist-ange-level-2",
    "https://www.tcgplayer.com/product/259360/wixoss-interlude-diva-assist-ange-level-2",
    "https://www.tcgplayer.com/product/259361/wixoss-interlude-diva-assist-ange-level-2-l",
    "https://www.tcgplayer.com/product/259484/wixoss-interlude-diva-assist-ange-level-2-parallel-foil",
    "https://www.tcgplayer.com/product/259485/wixoss-interlude-diva-assist-ange-level-2-parallel-foil-l",
    "https://www.tcgplayer.com/product/259331/wixoss-interlude-diva-assist-lize-level-1",
    "https://www.tcgplayer.com/product/259353/wixoss-interlude-diva-assist-lize-level-1-l",
    "https://www.tcgplayer.com/product/259476/wixoss-interlude-diva-assist-lize-level-1-parallel-foil",
    "https://www.tcgplayer.com/product/259477/wixoss-interlude-diva-assist-lize-level-1-parallel-foil-l",
    "https://www.tcgplayer.com/product/259352/wixoss-interlude-diva-assist-lize-level-2",
    "https://www.tcgplayer.com/product/259354/wixoss-interlude-diva-assist-lize-level-2-l",
    "https://www.tcgplayer.com/product/259355/wixoss-interlude-diva-assist-lize-level-2-wxdi-p00-028en",
    "https://www.tcgplayer.com/product/259478/wixoss-interlude-diva-assist-lize-level-2-parallel-foil",
    "https://www.tcgplayer.com/product/259480/wixoss-interlude-diva-assist-lize-level-2-parallel-foil-l",
    "https://www.tcgplayer.com/product/259481/wixoss-interlude-diva-assist-lize-level-2-parallel-foil-wxdi-p00-028pen",
    "https://www.tcgplayer.com/product/259288/wixoss-diva-debut-deck-d02-nijisanji-ver-sanbaka-assist-toko-level-1",
    "https://www.tcgplayer.com/product/259365/wixoss-interlude-diva-assist-toko-level-1",
    "https://www.tcgplayer.com/product/259486/wixoss-interlude-diva-assist-toko-level-1-parallel-foil",
    "https://www.tcgplayer.com/product/259289/wixoss-diva-debut-deck-d02-nijisanji-ver-sanbaka-assist-toko-level-2",
    "https://www.tcgplayer.com/product/259366/wixoss-interlude-diva-assist-toko-level-2",
    "https://www.tcgplayer.com/product/259367/wixoss-interlude-diva-assist-toko-level-2-l",
    "https://www.tcgplayer.com/product/259488/wixoss-interlude-diva-assist-toko-level-2-parallel-foil",
    "https://www.tcgplayer.com/product/259489/wixoss-interlude-diva-assist-toko-level-2-parallel-foil-l",
    "https://www.tcgplayer.com/product/259356/wixoss-interlude-diva-center-ange-level-1",
    "https://www.tcgplayer.com/product/259449/wixoss-interlude-diva-center-ange-level-1-scr",
    "https://www.tcgplayer.com/product/259357/wixoss-interlude-diva-center-ange-level-2",
    "https://www.tcgplayer.com/product/259450/wixoss-interlude-diva-center-ange-level-2-scr",
    "https://www.tcgplayer.com/product/259358/wixoss-interlude-diva-center-ange-level-3",
    "https://www.tcgplayer.com/product/259443/wixoss-interlude-diva-center-ange-level-3-dir",
    "https://www.tcgplayer.com/product/259451/wixoss-interlude-diva-center-ange-level-3-scr",
    "https://www.tcgplayer.com/product/259278/wixoss-diva-debut-deck-d02-nijisanji-ver-sanbaka-center-lize-level-1",
    "https://www.tcgplayer.com/product/259452/wixoss-interlude-diva-center-lize-level-1-scr",
    "https://www.tcgplayer.com/product/259280/wixoss-diva-debut-deck-d02-nijisanji-ver-sanbaka-center-lize-level-2",
    "https://www.tcgplayer.com/product/259453/wixoss-interlude-diva-center-lize-level-2-scr",
    "https://www.tcgplayer.com/product/259281/wixoss-diva-debut-deck-d02-nijisanji-ver-sanbaka-center-lize-level-3",
    "https://www.tcgplayer.com/product/259440/wixoss-interlude-diva-center-lize-level-3-dir",
    "https://www.tcgplayer.com/product/259454/wixoss-interlude-diva-center-lize-level-3-scr",
    "https://www.tcgplayer.com/product/259362/wixoss-interlude-diva-center-toko-level-1",
    "https://www.tcgplayer.com/product/259455/wixoss-interlude-diva-center-toko-level-1-scr",
    "https://www.tcgplayer.com/product/259363/wixoss-interlude-diva-center-toko-level-2",
    "https://www.tcgplayer.com/product/259456/wixoss-interlude-diva-center-toko-level-2-scr",
    "https://www.tcgplayer.com/product/259364/wixoss-interlude-diva-center-toko-level-3",
    "https://www.tcgplayer.com/product/259438/wixoss-interlude-diva-center-toko-level-3-dir",
    "https://www.tcgplayer.com/product/259457/wixoss-interlude-diva-center-toko-level-3-scr",
    "https://www.tcgplayer.com/product/239073/weiss-schwarz-bofuri-i-dont-want-to-get-hurt-so-ill-max-out-my-defense-deploy-left-arm",
    "https://www.tcgplayer.com/product/239074/weiss-schwarz-bofuri-i-dont-want-to-get-hurt-so-ill-max-out-my-defense-deploy-left-arm-rrr",
    "https://www.tcgplayer.com/product/277515/weiss-schwarz-is-it-wrong-to-try-to-pick-up-girls-in-a-dungeon-familia-myth",
    "https://www.tcgplayer.com/product/277460/weiss-schwarz-is-it-wrong-to-try-to-pick-up-girls-in-a-dungeon-futsu-no-mitama",
    "https://www.tcgplayer.com/product/277485/weiss-schwarz-is-it-wrong-to-try-to-pick-up-girls-in-a-dungeon-god-of-the-masses-ganesha",
    "https://www.tcgplayer.com/product/277404/weiss-schwarz-is-it-wrong-to-try-to-pick-up-girls-in-a-dungeon-hestia-familia",
    "https://www.tcgplayer.com/product/239003/weiss-schwarz-bofuri-i-dont-want-to-get-hurt-so-ill-max-out-my-defense-hydra-maple",
    "https://www.tcgplayer.com/product/277444/weiss-schwarz-is-it-wrong-to-try-to-pick-up-girls-in-a-dungeon-luminous-wind",
    "https://www.tcgplayer.com/product/277445/weiss-schwarz-is-it-wrong-to-try-to-pick-up-girls-in-a-dungeon-luminous-wind-rrr",
    "https://www.tcgplayer.com/product/277355/weiss-schwarz-is-it-wrong-to-try-to-pick-up-girls-in-a-dungeon-sword-princess-ais",
    "https://www.tcgplayer.com/product/277356/weiss-schwarz-is-it-wrong-to-try-to-pick-up-girls-in-a-dungeon-sword-princess-ais-sp",
    "https://www.tcgplayer.com/product/37817/magic-unhinged-_____",
    "https://www.tcgplayer.com/product/237278/pokemon-gym-challenge-______s-chansey",
    "https://www.tcgplayer.com/product/180718/pokemon-jumbo-cards-______s-oshawott",
    "https://www.tcgplayer.com/product/159115/pokemon-pikachu-world-collection-promos-______s-pikachu",
    "https://www.tcgplayer.com/product/250325/pokemon-celebrations-classic-collection-______s-pikachu",
    "https://www.tcgplayer.com/product/90784/pokemon-wotc-promo-______s-pikachu",
    "https://www.tcgplayer.com/product/211418/pokemon-jumbo-cards-______s-snivy",
    "https://www.tcgplayer.com/product/211419/pokemon-jumbo-cards-______s-tepig",
    "https://www.tcgplayer.com/product/243201/magic-adventures-in-the-forgotten-realms-plus2-mace",
    "https://www.tcgplayer.com/product/169764/star-wars-destiny-way-of-the-force-0-0-0",
    "https://www.tcgplayer.com/product/169765/star-wars-destiny-way-of-the-force-0-0-0-card-only",
    "https://www.tcgplayer.com/product/198850/star-wars-destiny-spark-of-hope-0-0-0-protocol-matrix",
    "https://www.tcgplayer.com/product/193904/star-wars-destiny-spark-of-hope-0-0-0-protocol-matrix-card-only",
    "https://www.tcgplayer.com/product/138803/metax-tcg-justice-league-1-intelligence-c32jl",
    "https://www.tcgplayer.com/product/162936/metax-tcg-attack-on-titan-1-intelligence-c33-at",
    "https://www.tcgplayer.com/product/162937/metax-tcg-attack-on-titan-1-intelligence-c34-at",
    "https://www.tcgplayer.com/product/168915/metax-tcg-batman-1-intelligence-c37-bm",
    "https://www.tcgplayer.com/product/168980/metax-tcg-batman-1-intelligence-r126-bm",
    "https://www.tcgplayer.com/product/138884/metax-tcg-justice-league-1-intelligence-r127jl",
    "https://www.tcgplayer.com/product/138904/metax-tcg-justice-league-1-intelligence-s15jl",
    "https://www.tcgplayer.com/product/163048/metax-tcg-attack-on-titan-1-intelligence-s30-at",
    "https://www.tcgplayer.com/product/138924/metax-tcg-justice-league-1-intelligence-s33jl",
    "https://www.tcgplayer.com/product/138943/metax-tcg-justice-league-1-intelligence-s50jl",
    "https://www.tcgplayer.com/product/138963/metax-tcg-justice-league-1-intelligence-s69jl",
]

column = ['Set Name', 'Card Name', 'URL', 'Image', 'Description']

with open('test.csv', 'w', newline = "", encoding="utf-8") as f:
    write = csv.writer(f)
    write.writerows([column])
    f.close()

def findIndex(ele, arr):
    return arr.index(ele)

def main(url):
    output = []
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "product-details__name")))
    except:
        try:
            driver.refresh()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "product-details__name")))
        except:
            print('Hit issue with URL sending to issueUrl.txt: ' + url)
            with open('issueCards.txt', 'a') as f:
                f.write(url + '\n')
            f.close()
    setNameGroup = driver.find_element(By.CLASS_NAME, 'product-details__name').text
    setNameSplit = setNameGroup.split(' - ')
    if len(setNameSplit) != 2:
        print('Hit issue with Set Name Split')
        driver.refresh()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "product-details__name")))
        setNameGroup = driver.find_element(By.CLASS_NAME, 'product-details__name').text
        setNameSplit = setNameGroup.split(' - ')
    card = setNameSplit[0]
    setName = setNameSplit[1]
    

    image = driver.find_element(By.CLASS_NAME, 'progressive-image-main').get_attribute('src')
    # imgD.main(image)

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
    
    # Split Elem 0 and Elem 1
    # Check length of each
    dataClean = []
    columnClean = []
    for i in pdList:
        ele = []
        text = i.text
        spl_one = text.split(':')
        idx = 0
        arr = ['','']
        for j in spl_one:
            if ' / ' in j:
                ele = j.split(' / ')
            elif '/ ' in j:
                ele = j.split('/ ')
            elif ' /' in j:
                ele = j.split(' /')
            else:
                ele = j
            arr[idx] = ele
            idx += 1                 

        # Need to check Length and fix if not same
        if type(arr[0]) == str and type(arr[1]) == str:
            if arr[0] not in column:
                column.append(arr[0])
            columnClean.append(arr[0])
            dataClean.append(arr[1])
        elif type(arr[0]) == list and type(arr[1]) == list:
            for l in arr[0]:
                if l not in column:
                    column.append(l)
                columnClean.append(l)
            for m in arr[1]:
                dataClean.append(m)
        else:
            if arr[0] not in column:
                column.append(arr[0])
            columnClean.append(arr[0])
            dataClean.append(arr[1])
        
        output = [''] * len(column)

    try:
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
    except:
        print('Hit issue with URL sending to issueCards.txt: ' + url)
        with open('issueCards.txt', 'a') as f:
            f.write(url + '\n')
        f.close()

for i in url:
    driver.get(i)
    main(i)

print(time.time() - start_time)