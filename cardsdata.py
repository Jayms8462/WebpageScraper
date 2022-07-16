import csv
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import concurrent.futures

start_time = time.time()

os.system('cls' if os.name == 'nt' else 'clear')
options = webdriver.FirefoxOptions()
# options.headless = True
driver = webdriver.Firefox(options = options)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}
url = [
    "https://www.tcgplayer.com/product/138900/metax-tcg-justice-league-1-strength-s11jl",
    "https://www.tcgplayer.com/product/138921/metax-tcg-justice-league-1-strength-s30jl",
    "https://www.tcgplayer.com/product/138939/metax-tcg-justice-league-1-strength-s47jl",
    "https://www.tcgplayer.com/product/138959/metax-tcg-justice-league-1-strength-s65jl",
    "https://www.tcgplayer.com/product/163087/metax-tcg-attack-on-titan-1-strength-u83-at",
    "https://www.tcgplayer.com/product/169020/metax-tcg-batman-1-strength-u85-bm",
    "https://www.tcgplayer.com/product/138838/metax-tcg-promotional-cards-1-strength-intelligence-special",
    # "https://www.tcgplayer.com/product/139002/metax-tcg-justice-league-1-strength-intelligence-special-u92jl",
    # "https://www.tcgplayer.com/product/121750/weiss-schwarz-nisekoi-extra-booster-1-10000-miracle-kosaki",
    # "https://www.tcgplayer.com/product/121751/weiss-schwarz-nisekoi-extra-booster-1-10000-miracle-kosaki-parallel-foil",
    # "https://www.tcgplayer.com/product/211214/weiss-schwarz-jojos-bizarre-adventure-golden-wind-10-hours-ago-pericolo",
    # "https://www.tcgplayer.com/product/211248/weiss-schwarz-jojos-bizarre-adventure-golden-wind-10-seconds-into-the-future",
    # "https://www.tcgplayer.com/product/211250/weiss-schwarz-jojos-bizarre-adventure-golden-wind-10-seconds-into-the-future-jjr",
    # "https://www.tcgplayer.com/product/229075/weiss-schwarz-mob-psycho-100-100pct-rrr",
    # "https://www.tcgplayer.com/product/96277/cardfight-vanguard-g-td03-flower-maiden-of-purity-100pct-orange",
    # "https://www.tcgplayer.com/product/146006/future-card-buddyfight-lvl-up-heroes-and-adventurers-100000-years-too-early",
    # "https://www.tcgplayer.com/product/134308/universus-mega-man-battle-for-power-1000-duels",
    # "https://www.tcgplayer.com/product/137289/future-card-buddyfight-chaos-control-crisis-100-dragon-overseer-of-mercenary-band-anthem-the-dual-sword",
    # "https://www.tcgplayer.com/product/102572/weiss-schwarz-attack-on-titan-104th-cadet-corps-class-annie",
    # "https://www.tcgplayer.com/product/102647/weiss-schwarz-attack-on-titan-104th-cadet-corps-class-bertholdt",
    # "https://www.tcgplayer.com/product/102623/weiss-schwarz-attack-on-titan-104th-cadet-corps-class-christa",
    # "https://www.tcgplayer.com/product/102624/weiss-schwarz-attack-on-titan-104th-cadet-corps-class-christa-sr",
    # "https://www.tcgplayer.com/product/102575/weiss-schwarz-attack-on-titan-104th-cadet-corps-class-conny",
    # "https://www.tcgplayer.com/product/102574/weiss-schwarz-attack-on-titan-104th-cadet-corps-class-eren",
    # "https://www.tcgplayer.com/product/102639/weiss-schwarz-attack-on-titan-104th-cadet-corps-class-jean",
    # "https://www.tcgplayer.com/product/102643/weiss-schwarz-attack-on-titan-104th-cadet-corps-class-marco",
    # "https://www.tcgplayer.com/product/102638/weiss-schwarz-attack-on-titan-104th-cadet-corps-class-mikasa",
    # "https://www.tcgplayer.com/product/102641/weiss-schwarz-attack-on-titan-104th-cadet-corps-class-reiner",
    # "https://www.tcgplayer.com/product/102633/weiss-schwarz-attack-on-titan-104th-cadet-corps-class-sasha",
    # "https://www.tcgplayer.com/product/102644/weiss-schwarz-attack-on-titan-104th-cadet-corps-class-ymir",
    # "https://www.tcgplayer.com/product/103279/weiss-schwarz-kancolle-10th-asashio-class-destroyer-kasumi",
    # "https://www.tcgplayer.com/product/179752/weiss-schwarz-kancolle-arrival-reinforcement-fleets-from-europe-10th-asashio-class-destroyer-kasumi-kai-ii",
    # "https://www.tcgplayer.com/product/179753/weiss-schwarz-kancolle-arrival-reinforcement-fleets-from-europe-10th-asashio-class-destroyer-kasumi-kai-ii-otsu",
    # "https://www.tcgplayer.com/product/103159/weiss-schwarz-kancolle-10th-ayanami-class-destroyer-ushio",
    # "https://www.tcgplayer.com/product/179774/weiss-schwarz-kancolle-arrival-reinforcement-fleets-from-europe-10th-ayanami-class-destroyer-ushio-kai-ii",
    # "https://www.tcgplayer.com/product/108715/weiss-schwarz-kancolle-2nd-fleet-10th-ayanami-class-destroyer-ushio-kai",
    # "https://www.tcgplayer.com/product/108654/weiss-schwarz-kancolle-2nd-fleet-10th-kagero-class-destroyer-tokitsukaze",
    # "https://www.tcgplayer.com/product/103218/weiss-schwarz-kancolle-10th-mutsuki-class-destroyer-mikaduki",
    # "https://www.tcgplayer.com/product/103280/weiss-schwarz-kancolle-10th-shiratsuyu-class-destroyer-suzukaze",
    # "https://www.tcgplayer.com/product/179839/weiss-schwarz-promo-cards-10th-shiratsuyu-class-destroyer-suzukaze-kai",
    # "https://www.tcgplayer.com/product/168413/dragon-ball-super-ccg-colossal-warfare-10x-kamehameha",
    # "https://www.tcgplayer.com/product/108681/weiss-schwarz-kancolle-2nd-fleet-11th-kagero-class-destroyer-urakaze",
    # "https://www.tcgplayer.com/product/103219/weiss-schwarz-kancolle-11th-mutsuki-class-destroyer-mochiduki",
    # "https://www.tcgplayer.com/product/108668/weiss-schwarz-kancolle-2nd-fleet-12th-kagero-class-destroyer-isokaze",
    # "https://www.tcgplayer.com/product/108669/weiss-schwarz-kancolle-2nd-fleet-12th-kagero-class-destroyer-isokaze-sr",
    # "https://www.tcgplayer.com/product/108655/weiss-schwarz-kancolle-2nd-fleet-12th-kagero-class-destroyer-isokaze-kai",
    # "https://www.tcgplayer.com/product/108682/weiss-schwarz-kancolle-2nd-fleet-13th-kagero-class-destroyer-hamakaze",
    # "https://www.tcgplayer.com/product/108683/weiss-schwarz-kancolle-2nd-fleet-13th-kagero-class-destroyer-hamakaze-sr",
    # "https://www.tcgplayer.com/product/134309/universus-red-horizon-tides-of-vengeance-13th-story-oblivion",
    # "https://www.tcgplayer.com/product/108684/weiss-schwarz-kancolle-2nd-fleet-14th-kagero-class-destroyer-tanikaze",
    # "https://www.tcgplayer.com/product/179727/weiss-schwarz-kancolle-arrival-reinforcement-fleets-from-europe-14th-yugumo-class-destroyer-okinami",
    # "https://www.tcgplayer.com/product/179754/weiss-schwarz-kancolle-arrival-reinforcement-fleets-from-europe-15th-kagero-class-destroyer-nowaki",
    # "https://www.tcgplayer.com/product/198127/universus-yu-yu-hakusho-16-instant-slashes",
    # "https://www.tcgplayer.com/product/179737/weiss-schwarz-kancolle-arrival-reinforcement-fleets-from-europe-16th-kagero-class-destroyer-arashi",
    # "https://www.tcgplayer.com/product/179776/weiss-schwarz-kancolle-arrival-reinforcement-fleets-from-europe-16th-yugumo-class-destroyer-asashimo",
    # "https://www.tcgplayer.com/product/179775/weiss-schwarz-kancolle-arrival-reinforcement-fleets-from-europe-16th-yugumo-class-destroyer-asashimo-kai",
    # "https://www.tcgplayer.com/product/179738/weiss-schwarz-kancolle-arrival-reinforcement-fleets-from-europe-17th-kagero-class-destroyer-hagikaze",
    # "https://www.tcgplayer.com/product/108670/weiss-schwarz-kancolle-2nd-fleet-17th-yugumo-class-destroyer-hayashimo",
    # "https://www.tcgplayer.com/product/103086/weiss-schwarz-kancolle-18th-kagero-class-destroyer-maikaze",
    # "https://www.tcgplayer.com/product/158466/magic-world-championship-decks-1996-bertrand-lestree-biography-card",
    # "https://www.tcgplayer.com/product/158469/magic-world-championship-decks-1996-bertrand-lestree-decklist-card",
    # "https://www.tcgplayer.com/product/158533/magic-world-championship-decks-1996-eric-tam-biography-card",
    # "https://www.tcgplayer.com/product/158534/magic-world-championship-decks-1996-eric-tam-decklist-card",
    # "https://www.tcgplayer.com/product/158597/magic-world-championship-decks-1996-george-baxter-biography-card",
    # "https://www.tcgplayer.com/product/158598/magic-world-championship-decks-1996-george-baxter-decklist-card",
    # "https://www.tcgplayer.com/product/158664/magic-world-championship-decks-1996-leon-lindback-biography-card",
    # "https://www.tcgplayer.com/product/158665/magic-world-championship-decks-1996-leon-lindback-decklist-card",
    # "https://www.tcgplayer.com/product/159165/magic-world-championship-decks-1996-mark-justice-biography-card",
    # "https://www.tcgplayer.com/product/159166/magic-world-championship-decks-1996-mark-justice-decklist-card",
    # "https://www.tcgplayer.com/product/159223/magic-world-championship-decks-1996-michael-loconto-biography-card",
    # "https://www.tcgplayer.com/product/159229/magic-world-championship-decks-1996-michael-loconto-decklist-card",
    # "https://www.tcgplayer.com/product/159276/magic-world-championship-decks-1996-preston-poulter-biography-card",
    # "https://www.tcgplayer.com/product/159277/magic-world-championship-decks-1996-preston-poulter-decklist-card",
    # "https://www.tcgplayer.com/product/160821/magic-world-championship-decks-1996-shawn-hammer-regnier-biography-card",
    # "https://www.tcgplayer.com/product/160822/magic-world-championship-decks-1996-shawn-hammer-regnier-decklist-card",
    # "https://www.tcgplayer.com/product/21655/magic-special-occasion-1996-world-champion",
    # "https://www.tcgplayer.com/product/158471/magic-world-championship-decks-1996-world-championship-blank-card",
    # "https://www.tcgplayer.com/product/162291/magic-world-championship-decks-1997-jakub-slemr-biography-card",
    # "https://www.tcgplayer.com/product/162292/magic-world-championship-decks-1997-jakub-slemr-decklist-card",
    # "https://www.tcgplayer.com/product/162436/magic-world-championship-decks-1997-janosch-kuhn-biography-card",
    # "https://www.tcgplayer.com/product/162437/magic-world-championship-decks-1997-janosch-kuhn-decklist-card",
    # "https://www.tcgplayer.com/product/162760/magic-world-championship-decks-1997-paul-mccabe-biography-card",
    # "https://www.tcgplayer.com/product/162761/magic-world-championship-decks-1997-paul-mccabe-decklist-card",
    # "https://www.tcgplayer.com/product/164432/magic-world-championship-decks-1997-svend-geertsen-biography-card",
    # "https://www.tcgplayer.com/product/164433/magic-world-championship-decks-1997-svend-geertsen-decklist-card",
    # "https://www.tcgplayer.com/product/161069/magic-world-championship-decks-1997-world-championship-advertisement-card",
    # "https://www.tcgplayer.com/product/161068/magic-world-championship-decks-1997-world-championship-blank-card",
    # "https://www.tcgplayer.com/product/164554/magic-world-championship-decks-1998-ben-rubin-biography-card",
    # "https://www.tcgplayer.com/product/164555/magic-world-championship-decks-1998-ben-rubin-decklist-card",
    # "https://www.tcgplayer.com/product/164581/magic-world-championship-decks-1998-brian-hacker-biography-card",
    # "https://www.tcgplayer.com/product/164582/magic-world-championship-decks-1998-brian-hacker-decklist-card",
    # "https://www.tcgplayer.com/product/163933/magic-world-championship-decks-1998-brian-selden-biography-card",
    # "https://www.tcgplayer.com/product/163934/magic-world-championship-decks-1998-brian-selden-decklist-card",
    # "https://www.tcgplayer.com/product/164633/magic-world-championship-decks-1998-randy-buehler-biography-card",
    # "https://www.tcgplayer.com/product/164634/magic-world-championship-decks-1998-randy-buehler-decklist-card",
    # "https://www.tcgplayer.com/product/189746/magic-world-championship-decks-1998-world-championship-advertisement-card",
    # "https://www.tcgplayer.com/product/181671/magic-world-championship-decks-1998-world-championship-blank-card",
    # "https://www.tcgplayer.com/product/164929/magic-world-championship-decks-1999-jakub-slemr-biography-card",
    # "https://www.tcgplayer.com/product/164930/magic-world-championship-decks-1999-jakub-slemr-decklist-card",
    # "https://www.tcgplayer.com/product/164407/magic-world-championship-decks-1999-kai-budde-biography-card"
]

column = ['Set Name', 'Card Name', 'Image', 'Description', 'Card Attributes']

with open('test.csv', 'w', newline = "", encoding="utf-8") as f:
    write = csv.writer(f)
    write.writerows([column])
    f.close()

def main(url, issueCount):
    # Grabs Card Name and Set Name
    try:
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

        # Grabs Image
        image = driver.find_element(By.CLASS_NAME, 'progressive-image-main').get_attribute('src')

        # Toggle for Read Me to grab all the data
        try:
            readMore = driver.find_element(By.CLASS_NAME, 'product__item-details__toggle.masked')
            readMore.click()
        except NoSuchElementException:
            readMore = ''

        # Grabs Description
        try:
            description = driver.find_element(By.CLASS_NAME, 'product__item-details__description').text
        except:
            description = ''

        # Grabs Attributes of Card
        dataAttributes = driver.find_element(By.CLASS_NAME, 'product__item-details__attributes').text

        output = [setName, card, image, description, dataAttributes]

        with open('test.csv', 'a', newline = "", encoding="utf-8") as f:
            write = csv.writer(f)
            write.writerows([output])
            f.close()

        print('Completed ', url)
    except:
        issueCount += 1

        if issueCount <= 3:
            print('Hit issue with URL sending to issueUrl.txt: ' + url)
            print('Trying Url again, attempt:', issueCount)
        else:
            print('Could not resolve issue:', url)
            with open('issueCards.txt', 'a') as f:
                f.write(url + '\n')
            f.close()

for i in url:
    issueCount = 0
    driver.get(i)
    main(i, issueCount)


total_time = time.time() - start_time

print(total_time)