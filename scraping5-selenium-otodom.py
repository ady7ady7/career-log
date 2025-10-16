

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
    print(f'Obecna lista mieszkań: {len(linki)} linków')
    print(linki)

except Exception as e:
    print(f'Error: {(e)}')


try:
    original_window = driver.current_window_handle
    opisy = []
    filtered_linki = []
    
    for i in linki:
        
        driver.execute_script(f"window.open('{i}')")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)

        #FILTROWANIE 1 - SPRAWDZAMY SEKCJĘ INFORMACJE DODATKOWE - NIE CHCĘ, ABY BYŁ TU GARAŻ
        info_dodatkowe = driver.find_elements(By.CLASS_NAME, 'e1mm5aqc1')
        has_garaz = any('garaż' in (e.get_attribute('textContent') or '').lower() #thanks to Claude for this one!
                for e in info_dodatkowe)
        time.sleep(1)
        if has_garaz:
            print("Jest garaż w górnej sekcji, do widzenia!")
            driver.close()
            driver.switch_to.window(original_window)
            continue #kolejny link
        else:
            print("Nie ma garażu, szukamy dalej...")
        
        
        #SCRAPUJEMY OPIS Z OGŁOSZENIA
             
        time.sleep(1)    
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
                print("Scrolling to our button") #Komentarz poglądowy, tak naprawdę do wywalenia
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
        opisy.append(opis)
        filtered_linki.append(i) #Dodajemy tutaj nasz link do filtered_linki, żeby naprawić błąd z wstawianiem niewyfiltrowanych linków
        print(f"Scraped from {i}: {opis[:100]}...") #Printujemy pierwsze 100 znaków, poglądowo, do wywalenia
        driver.close()
        driver.switch_to.window(original_window)
except Exception as e:
    print(f'Error: {(e)}')
   
if len(opisy) < len(filtered_linki):
    while len(opisy) < len(filtered_linki):
        opisy.append("Nie ma opisu :(")
    
df = pd.DataFrame({
    'link': filtered_linki,
    'opis': opisy
})

###Tutaj chcemy ogarnąć sortowanie
filters = ['garaż', 'parking podziemny', 'miejsce podziemne']
df = df[df['opis'].str.contains('|'.join(filters), case=False, na=False)]
df.to_csv('mieszkania_otodom.csv', index=False, encoding='utf-8')
###Trzeba będzie jeszcze zrobić sortowanie strefy na górze ogłoszenia (DONE) i paginację, ewentualnie jeszcze tytuł

print(df)
    
    
