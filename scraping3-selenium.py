from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
url = 'https://www.filmweb.pl/ranking/premiere/serial'
driver=webdriver.Chrome(options=options)
driver.get(url=url)

cookie_button = driver.find_element(By.CLASS_NAME,'highlight-button')
time.sleep(1)
cookie_button.click()
time.sleep(1)
print('Cookie button skipped')

try:  
    adscreen = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'preventScroll')))
    time.sleep(2) #ten wait tutaj wydaje się być bardzo ważny, bez tego strona chyba nie zdąża sie doładować i wywala błąd - pewnie dlatego, że ogólnie przycisk jest wyszarzony - w razie problemów zwiększyć czas o sekundę-dwie i będzie ok!
    adskip_button = driver.find_element(By.CSS_SELECTOR, 'body > div.faInterstitialDesktop > div > div.faInterstitialDesktop__header > div > button')
    adskip_button.click()
    print('Ad button skipped')
except Exception as e:
    print(f"Error: {str(e)}")

lista = driver.find_element(By.CLASS_NAME, 'rankingTypeSection__container')
seriale = lista.find_elements(By.CLASS_NAME, 'rankingType__card')
for serial in seriale:
    serial_pos_title = serial.find_element(By.CLASS_NAME, 'rankingType__title').text
    serial_score = serial.find_element(By.CLASS_NAME, 'rankingType__rate--value').text
    #serial_pic = serial.find_element(By.CLASS_NAME, 'efficientPoster__wrapper.data-image')
    print(f"Top {serial_pos_title}, ocena {serial_score}")
    
    

