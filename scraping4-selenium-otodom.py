

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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
    mieszkania = driver.find_elements(By.CLASS_NAME, 'e19ka3dj0')
    #original_window = driver.current_window_handle
    for mieszkanie in mieszkania:
        link = mieszkanie.find_element(By.CLASS_NAME, 'css-ito1if')
        link.click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(1)
        container = driver.find_element(By.CLASS_NAME, 'e1op7yyl0')
        showmore_btn = container.find_element(By.CLASS_NAME, 'css-8q56v9')
        print('Button located, clicking in 1 sec')
        time.sleep(1)
        showmore_btn.click()
        opis = driver.find_element(By.CLASS_NAME, 'e1op7yyl1').text
        print(opis)
        #driver.switch_to.window(original_window)
except Exception as e:
    print(f'Error: {(e)}')