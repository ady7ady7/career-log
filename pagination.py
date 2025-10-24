


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

#Skip przycisku ciasteczkowego
try:
    cookie_button = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
    cookie_button.click()
    print('Cookie button skipped')
    time.sleep(2)
except Exception as e:
    print(f'Error: {(e)}')
    
    
#aktywny przycisk = class="css-jayau4"
current_page_number = int(driver.find_element(By.CLASS_NAME, 'css-jayau4').text)
max_pages = 50

while current_page_number <= max_pages:
        print('Czekamy 5 sekund profilaktycznie, żeby się załadowało')
        time.sleep(5)
        current_page = driver.find_element(By.CLASS_NAME, 'css-jayau4') #tutaj ważne rozróżnienie - nie dodajemy .text, bo się wykrzaczy
        current_page_number = int(current_page.text) #tutaj robimy oddzielną zmienną, żeby wyciągnąć tekst, a potem konwertujemy to na int, żeby porównania działały
        print(f'Jesteśmy obecnie na stronie {current_page_number}')
        if current_page_number <= max_pages:
            try: 
                print(f'Czekamy 5 sekund, żeby się wszystko załadowało $1')
                time.sleep(5)
                pagination_panel = driver.find_element(By.CLASS_NAME, 'css-iiviho')
                pagination_buttons = pagination_panel.find_elements(By.CLASS_NAME, 'css-10sgmrs')
                next_page_button = pagination_buttons[-1]

                if next_page_button:
                    print(f'Czekamy 5 sekund, żeby się wszystko załadowało $2')
                    time.sleep(5)
                    print(f'The current_page number is {current_page_number}, found next page button, scrolling to it in 1 sec')
                    time.sleep(1)
                    driver.execute_script("""arguments[0].scrollIntoView({
                        behavior: 'smooth',
                        block: 'center',
                        inline: 'center'});
                        """, next_page_button)
                    print(f'Czekamy 5 sekund, żeby się wszystko załadowało #3 - powinniśmy być zescrollowani do kolejnego przycisku teraz')
                    time.sleep(5)
                    driver.execute_script('arguments[0].click();', next_page_button)
                else:
                    print('The next page button is not available, so we probably got all of the pages down!')
                
            except Exception as e:
                print(f'Error: {(e)}')
                print(f'Nie ma kolejnego przycisku, skończyliśmy po {current_page} stronach')
                break
    
    
    #SCROLLOWANIE JEST GIT
    #PRAWDOPODOBNIE KULEJE KLIKANIE I WRACAMY DO PIERWSZEJ STRONY, ZAMIAST DO