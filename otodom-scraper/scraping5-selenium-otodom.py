

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time
import pandas as pd
import random #dodałem żeby randomizować waita przy paginacji, na razie nie widzę żadnych problemów, czy limitów, ale dodałem to tak w razie co

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
    
    
wszystkie_opisy = []
wszystkie_wyfiltrowane_linki = []
calkowita_liczba_linkow = 0

current_page_number = int(driver.find_element(By.CLASS_NAME, 'css-jayau4').text)
max_pages = 70

try:
    while current_page_number <= max_pages:
        print('Czekamy 5 sekund na załadowanie się strony')
        time.sleep(5)
        current_page = driver.find_element(By.CLASS_NAME, 'css-jayau4') #tutaj ważne rozróżnienie - nie dodajemy .text, bo się wykrzaczy
        current_page_number = int(current_page.text) #tutaj robimy oddzielną zmienną, żeby wyciągnąć tekst, a potem konwertujemy to na int, żeby porównania działały
        print(f'Jestesmy na stronie {current_page_number}')
        
        
        #ogarnianie listy mieszkań ze strony    
        try:
            lista = []
            current_height = driver.execute_script("return document.body.scrollHeight")
            
            while True:
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                time.sleep(1)
                new_height = driver.execute_script("return document.body.scrollHeight")
                print(f'New height: {new_height}, Current height: {current_height}')
                if current_height == new_height:
                    break
                current_height = new_height
                
            
            mieszkania = driver.find_elements(By.CLASS_NAME, 'css-ito1if')
            for mieszkanie in mieszkania:
                link = mieszkanie.find_element(By.TAG_NAME, 'a')
                href = link.get_attribute('href')
                lista.append(href)

            
            linki = pd.Series(lista).drop_duplicates().tolist()
            calkowita_liczba_linkow += len(linki)
            print(f'Strona {current_page}, obecna lista mieszkań: {len(linki)} linków')
            print(linki)

        except Exception as e:
            print(f'Error: {(e)}')

        #Tutaj dodajemy handle do naszego bazowego okna (może się to zmienić przy paginacji)
        #original_window = driver.current_window_handle
        
        for i in linki:
            
            original_window = driver.current_window_handle #przerzucamy tutaj, bo zdaje się, że to mogło blokować całą pętlę przy paginacji na stronach 1-2
            driver.execute_script(f"window.open('{i}')")
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(1)

            #FILTROWANIE 1 - SPRAWDZAMY SEKCJĘ INFORMACJE DODATKOWE - NIE CHCĘ, ABY BYŁ TU GARAŻ
            info_dodatkowe = driver.find_elements(By.CLASS_NAME, 'e1mm5aqc1')
            has_garaz = any('garaż' in (e.get_attribute('textContent') or '').lower() #thanks to Claude for this one!
                    for e in info_dodatkowe)
            time.sleep(2)
            if has_garaz:
                print("Jest garaż w górnej sekcji, do widzenia!")
                driver.close()
                driver.switch_to.window(original_window)
                continue #kolejny link
            else:
                print("Nie ma garażu, szukamy dalej...")
            
            #SCRAPUJEMY OPIS Z OGŁOSZENIA 
            ###################### TRY EXCEPT BLOCK DODANY ###############################
            #Dodany tutaj try-except block, żeby error404 na pojedynczej stronie nie wywalał działania kodu
            try:   
                time.sleep(2)    
                container = driver.find_element(By.CLASS_NAME, 'e1op7yyl0')
                button_enabled = False #DOMYŚLNIE USTAWIAMY SOBIE TAKIEGO BOOLA, ZMIENIMY WARTOŚĆ PO PRZESCROLLOWANIU KLIKNIĘCIU PRZYCISKU
                
                while not button_enabled:
                    try: #Scrollowanie do przycisku z Pokaż więcej (opis) i kliknięcie go, ta cała procedura była wymagana, ponieważ ogłoszenia miały różną długośc i z góry ustalona odległość zwyczajnie czasem się wykrzaczała
                        showmore_btn = container.find_element(By.CLASS_NAME, 'css-8q56v9') #NIŻEJ UŻYTY SCROLL Z JAVASCRIPT - NAJPEWNIEJSZA OPCJA - DZIAŁA BEZPOŚREDNIO W JS PRZEGLĄDARKI, A NIE Z POZIOMU NASZEGO SERWERA
                        driver.execute_script("""arguments[0].scrollIntoView({
                            behavior: 'smooth',
                            block: 'center',
                            inline: 'center'});
                            """, showmore_btn)
                        wait = WebDriverWait(driver, 2)
                        clickable_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-8q56v9')))
                        time.sleep(0.5) #Sleepy można pewnie usunąć, ale to nie musi być idealnie zoptymalizowane + faktycznie były momenty w trakcie pracy, że sleep robił różnicę, bo coś się jeszce nie zdążyło załadować
                        driver.execute_script('arguments[0].click();', showmore_btn) #znów używamy JS, bez tego potrafił być problem czasem - to jest konsekwentnie skuteczna metoda
                        time.sleep(1)
                        button_enabled = True #no i zmieniamy wartość boola, żeby odblokować dalszą część kodu
                    except Exception as e:
                        print(f"Attempt failed: {e}")
                        pass
                    time.sleep(0.5)
                    
                time.sleep(0.5)               
                opis = driver.find_element(By.CLASS_NAME, 'e1op7yyl1').text
                wszystkie_opisy.append(opis)
                wszystkie_wyfiltrowane_linki.append(i) #Dodajemy tutaj nasz link do filtered_linki, żeby naprawić błąd z wstawianiem niewyfiltrowanych linków
                print(f"Scraped from {i}: {opis[:100]}...") #Printujemy pierwsze 100 znaków, poglądowo, do wywalenia
            except Exception as e:
                print(f'Unable to locate element on {i}, skipping {e}')
            finally:
                driver.close()
                driver.switch_to.window(original_window)
            
        #PAGINACJA - FRAGMENT 2 - NA TYM ETAPIE PRZECHODZIMY DO KOLEJNEJ STRONY
        wait_time = random.randrange(10, 17)
        print(f'Czekamy {wait_time} sekund profilaktycznie, żeby nie przekroczyć limitów')
        time.sleep(15)
        if current_page_number <= max_pages:
            try: 
                pagination_panel = driver.find_element(By.CLASS_NAME, 'css-iiviho')
                pagination_buttons = pagination_panel.find_elements(By.CLASS_NAME, 'css-10sgmrs')
                next_page_button = pagination_buttons[-1]

                if next_page_button:
                    print(f'Obecnie jesteśmy na stronie {current_page_number}, scrollujemy do przycisku za 1s')
                    time.sleep(1)
                    driver.execute_script("""arguments[0].scrollIntoView({
                        behavior: 'smooth',
                        block: 'center',
                        inline: 'center'});
                        """, next_page_button)
                    print('Klikamy za sekundę')
                    time.sleep(1)
                    driver.execute_script('arguments[0].click();', next_page_button)
                else:
                    print('Nie ma kolejnego przycisku, przeszliśmy wybrany zakres stron.')
                
            except Exception as e:
                print(f'Error: {(e)}')
                print(f'Nie ma kolejnego przycisku, skończyliśmy po {current_page_number} stronach')
                break

except Exception as e:
    print(f'Wystąpił nieoczekiwany błąd podczas scrapingu na stronie {current_page_number}: {e}')
    print('Zapisujemy dane w obecnym stanie.')
except KeyboardInterrupt as e:
    print('Manualnie zatrzymano działanie kodu.')
finally: 
    if len(wszystkie_opisy) < len(wszystkie_wyfiltrowane_linki):
        while len(wszystkie_opisy) < len(wszystkie_wyfiltrowane_linki):
            wszystkie_opisy.append("Nie ma opisu :(")
        
    df = pd.DataFrame({
        'link': wszystkie_wyfiltrowane_linki,
        'opis': wszystkie_opisy
    })

    procent_linków = len(wszystkie_wyfiltrowane_linki)/calkowita_liczba_linkow*100
    print(f'Zakończyliśmy scraping na stronie {current_page_number}. Przeprocesowaliśmy {calkowita_liczba_linkow}, wybierając ostatecznie {len(wszystkie_wyfiltrowane_linki)}, co oznacza wytypowanie {procent_linków} procent linków')
    ###Tutaj chcemy ogarnąć sortowanie
    filters = ['garaż', 'parking podziemny', 'miejsce podziemne']
    df = df[df['opis'].str.contains('|'.join(filters), case=False, na=False)]
    df.to_csv('mieszkania_otodom.csv', index=False, encoding='utf-8')
    ###Trzeba będzie jeszcze zrobić sortowanie strefy na górze ogłoszenia (DONE) i paginację, ewentualnie jeszcze tytuł


    print(df)