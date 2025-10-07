#attempt 2 - the goal is to scrape the list of premieres

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
url = 'https://www.filmweb.pl/ranking/premiere'
driver=webdriver.Chrome(options=options)
driver.get(url)



try:
    time.sleep(3)
    clickable = driver.find_element(By.XPATH, '//*[@id="didomi-notice-agree-button"]')
    time.sleep(1)
    clickable.click()
    print ('Filmweb cookie button skipped')
    
    time.sleep(10)
    ad = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,'preventScroll')))
    print('ad present & located, waiting 3 sec')
    time.sleep(3)
    adskip_button = driver.find_element(By.CSS_SELECTOR, 'body > div.faInterstitialDesktop > div > div.faInterstitialDesktop__header > div > button')
    adskip_button.click()
    print ('Filmweb ad screen skipped')
    #PROGRESS - WE MANAGED TO ACTUALLY WAIT UNTIL THE AD SCREEN AND SKIP IT PROPERLY!!!
    

    list=driver.find_element(By.CLASS_NAME, "rankingTypeSection__container")
    print(f'List located {list}')
    films = list.find_elements(By.CLASS_NAME, 'rankingType__card')
    #We're good here
    # film_title=films.find_element(By.CSS_SELECTOR, 'div.page__container.rankingTypeSection__container > div:nth-child(1) > div.rankingType__card > div.rankingType__header > div > h2 > a')
    # film_score=films.find_element(By.CSS_SELECTOR, 'div.page__container.rankingTypeSection__container > div:nth-child(1) > div.rankingType__card > div.rankingType__rateWrapper > a > div > span.rankingType__rate--value')
    #THE ISSUE IS THAT WE CANNOT use find_elemement on list! films is a list, so we can iterate through it and extract each title and score using find_element on THE CURRENT CARD!!!
    #The only issue I have now is to correctly identify and use the selector - whether CSS, CLASS, XPATH, or whatever - the last approach did not work
    
    for i in films:
        film_title=i.find_element(By.CSS_SELECTOR, 'div.page__container.rankingTypeSection__container > div:nth-child > div.rankingType__card > div.rankingType__header > div > h2 > a')
        film_score=i.find_element(By.CSS_SELECTOR, 'div.page__container.rankingTypeSection__container > div:nth-child > div.rankingType__card > div.rankingType__rateWrapper > a > div > span.rankingType__rate--value')

        print(f'Title = {film_title}')
        print(f'Ocena = {film_score}')
        
        
except Exception as e:
    print(f"Error: {str(e)}")