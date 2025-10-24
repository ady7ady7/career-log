


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
        print('Czekamy 5 sekund profilaktycznie, żeby się załadowało #1 - ten wait na pewno jest potrzebny akurat - może ewentualnie krótszy')
        time.sleep(5)
        current_page = driver.find_element(By.CLASS_NAME, 'css-jayau4') #tutaj ważne rozróżnienie - nie dodajemy .text, bo się wykrzaczy
        current_page_number = int(current_page.text) #tutaj robimy oddzielną zmienną, żeby wyciągnąć tekst, a potem konwertujemy to na int, żeby porównania działały
        print(f'Jesteśmy obecnie na stronie {current_page_number}')
        
        
        
        if current_page_number <= max_pages:
            try: 
                print(f'Wait zmniejszony z 5s do 2s #1')
                time.sleep(2)
                pagination_panel = driver.find_element(By.CLASS_NAME, 'css-iiviho')
                pagination_buttons = pagination_panel.find_elements(By.CLASS_NAME, 'css-10sgmrs')
                next_page_button = pagination_buttons[-1]

                if next_page_button:
                    print('Usunięty wait 5s #2')
                    print(f'Obecnie jesteśmy na stronie {current_page_number}, scrollujemy do przycisku za 1s')
                    print('Wait 1s')
                    time.sleep(1)
                    driver.execute_script("""arguments[0].scrollIntoView({
                        behavior: 'smooth',
                        block: 'center',
                        inline: 'center'});
                        """, next_page_button)
                    print(f'Usunięty wait 5s #3')
                    driver.execute_script('arguments[0].click();', next_page_button)
                else:
                    print('The next page button is not available, so we probably got all of the pages scraped!')
                
            except Exception as e:
                print(f'Error: {(e)}')
                print(f'Nie ma kolejnego przycisku, skończyliśmy po {current_page} stronach')
                break
    
    
    #Przekopiowuję sobie te fragmenty kodu tutaj, żeby było łatwiej - potem wszystko wróci do całości; docelowo pewnie i tak klasy i oddzielne pliki, ale to jest na tyle krótkie, że imo czytelne i ma to sens w obecnej formie
    #SCROLLOWANIE JEST GIT
    #ALE JESTEM ZLOOPOWANY NA STRONACH 1-2, TRZEBA TO ZDIAGNOZOWAĆ I NAPRAWIĆ
    
    #EDIT-- Dość szybko okazało się, że problem wynikał z klikania przycisku do poprzedniej strony - pominąłem go w pierwszej chwili, bo pojawiał się dopiero od drugiej strony, ale miał taką samą klasę.
    #Kombinowałem najpierw, ale najprostsze wydaje mi się ustawienie go jako ostatni przycisk [-1] - nie ma już innych przycisków o tej klasie, więc to fajnie działa.
    #Dodatkowo przy okazji ofc wywaliłem hardcodowaną liczbę current_page_number i podmieniłem ją po prostu za realną wartość z aktualnie aktywnego przycisku (ma odmienną klasę, fajnie)
    #Przy tej całej operacji pojawiły się też problemy z porównywaniem intów i stringów, bo na początku chwytałem przycisk current_page i wyciągałem z tego .text
    # aby to sfixować, stworzyłem odmienną zmienną current_page_number, gdzie mamy po prostu int(blabla_chwytanie_przycisku.text) - nie wiem, czy da się prościej, ale imo jest spoko.