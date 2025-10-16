

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
    
    for i in linki:
        
        driver.execute_script(f"window.open('{i}')")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)
    
        #Filtrowanie tego konkretnego okienka wydaje się być trudne, bo XPATH i CSS będą zmienne, a poszczególne entriesy mają identyczną klasę
        #XPATH: //*[@id="__next"]/div[1]/main/div[5]/div[1]/div[2]/div[1]/div[21]/div[2]
        #XPATH2: //*[@id="__next"]/div[1]/main/div[4]/div[1]/div[2]/div[1]/div[21]/div[2]
        #CSS-SEL2: #__next > div.css-2wgx6l.efze3g60 > main > div.css-tn073k.edmrbam0 > div.css-1w41ge1.edmrbam1 > div.css-1wo7cpa.e1mm5aqc0 > div:nth-child(2) > div:nth-child(21) > div:nth-child(2)
        #Trzeba przefiltrować wszystkie te elementy i poszukać słowa, które mnie interesuje - to !chyba! najprostsze rozwiązanie na ten moment
        
        sekcja_z_info_dod = driver.find_element(By.CLASS_NAME, 'e1mm5aqc0')
        driver.execute_script("""arguments[0].scrollIntoView({
                    behavior: 'smooth',
                    block: 'center',
                    inline: 'center'});
                    """, sekcja_z_info_dod)
        #info_dodatkowe = driver.find_elements(By.CLASS_NAME, 'e1mm5aqc1')\
        time.sleep(2)
        info_dodatkowe = driver.find_elements(By.CLASS_NAME, 'e1mm5aqc4')
        has_garaz = any('garaż' in (e.get_attribute('textContent') or '').lower()
                for e in info_dodatkowe)
        time.sleep(1)
        if has_garaz:
            print("Jest garaż w górnej sekcji, do widzenia!")
            driver.close()
            driver.switch_to.window(original_window)
            continue
        else:
            print("Nie ma garażu, szukamy dalej...")
        
        #FILTROWNAIE JEST OBECNIE NIESKUTECZNE TZN. Przepuszcza linki z garażem w sekcji Informacje dodatkowe - chyba trzeba znowu zrobić scrollIntoView, bo może to właśnie znów jest problem
            
        time.sleep(1)    
        container = driver.find_element(By.CLASS_NAME, 'e1op7yyl0')
        button_enabled = False
        
        while not button_enabled:
            try:
                showmore_btn = container.find_element(By.CLASS_NAME, 'css-8q56v9')
                driver.execute_script("""arguments[0].scrollIntoView({
                    behavior: 'smooth',
                    block: 'center',
                    inline: 'center'});
                    """, showmore_btn)
                print("Scrolling to our button")
                wait = WebDriverWait(driver, 2)
                clickable_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'css-8q56v9')))
                time.sleep(0.5)
                driver.execute_script('arguments[0].click();', showmore_btn)
                time.sleep(1)
                button_enabled = True
            except Exception as e:
                print(f"Attempt failed: {e}")
                pass
            time.sleep(0.5)
            
        time.sleep(0.5)               
        opis = driver.find_element(By.CLASS_NAME, 'e1op7yyl1').text
        opisy.append(opis)
        print(f"Scraped from {i}: {opis[:100]}...") #Printujemy pierwsze 100 znaków, żeby mieć poglądowo
        driver.close()
        driver.switch_to.window(original_window)
except Exception as e:
    print(f'Error: {(e)}')
   
if len(opisy) < len(linki):
    while len(opisy) < len(linki):
        opisy.append("Nie ma opisu :(")
    
df = pd.DataFrame({
    'link': linki,
    'opis': opisy
})

###Tutaj chcemy ogarnąć sortowanie
filters = ['garaż', 'parking podziemny', 'miejsce podziemne']
df = df[df['opis'].str.contains('|'.join(filters), case=False, na=False)]
df.to_csv('mieszkania_otodom.csv', index=False, encoding='utf-8')
###Trzeba będzie jeszcze zrobić sortowanie strefy na górze ogłoszenia i paginację

print(df)
    
    
