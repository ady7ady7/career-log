

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
url = 'https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/mazowieckie/warszawa/warszawa/warszawa?limit=36&ownerTypeSingleSelect=ALL&areaMin=60&buildYearMin=1999&roomsNumber=%5BTHREE%2CFOUR%5D&priceMax=1500000&by=DEFAULT&direction=DESC'
driver=webdriver.Chrome(options=options)
driver.get(url)

try:
    cookie_button = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
    cookie_button.click()
    print('Cookie button skipped')
    time.sleep(2)
except Exception as e:
    print(f'Error: {(e)}')
    
    
try:
    lista = []
    current_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        driver.execute_script('window.scrollTo(1000, document.body.scrollHeight)')
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if current_height == new_height:
            break
        last_height = new_height
        
    
    mieszkania = driver.find_elements(By.CLASS_NAME, 'css-ito1if')
    for mieszkanie in mieszkania:
        link = mieszkanie.find_element(By.TAG_NAME, 'a')
        href = link.get_attribute('href')
        lista.append(href)

    
    linki = pd.Series(lista).drop_duplicates()
    print(f'Obecna lista mieszkań: {len(linki)} linków')
    print(linki)

except Exception as e:
    print(f'Error: {(e)}')


try:
    original_window = driver.current_window_handle
    opisy = []
    for i in linki:
        driver.execute_script(f"window.open('{i}')")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)
        container = driver.find_element(By.CLASS_NAME, 'e1op7yyl0')
        
        #Scrollowanie po kawałku, az trafimy na przycisk
        button_enabled = False
        while not button_enabled:
            driver.execute_script("window.scrollTo(0, 300)")
            try:
                showmore_btn = container.find_element(By.CLASS_NAME, 'css-8q56v9')
                if showmore_btn.is_enabled():
                    button_enabled = True
                    print("The button is now enabled!")
            except:
                pass
            
        # time.sleep(1)
        # container = driver.find_element(By.CLASS_NAME, 'e1op7yyl0')
        # showmore_btn = container.find_element(By.CLASS_NAME, 'css-8q56v9')
        # print('Button located, clicking in 1 sec')
        time.sleep(1)
        showmore_btn.click()
        opis = driver.find_element(By.CLASS_NAME, 'e1op7yyl1').text
        opisy.append(opis)
        print(opis)
        time.sleep(1)
        driver.close()
        driver.switch_to.window(original_window)
except Exception as e:
    print(f'Error: {(e)}')
    
    print("Finished the procedure, printing opisy")
    print(opisy)
    
    
