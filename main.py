from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import time


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_experimental_option('excludeSwitches', ['enable-logging'])
url = 'https://www.wakacje.pl/lastminute/'
try:
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)
    ciasteczka = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[3]/div/button[1]')
    ciasteczka.click()
    
    #elems = driver.find_elements(By.XPATH,'//*[@id="__next"]/div/div[1]/main/div/div[2]/section/section')
    elems = driver.find_elements(By.XPATH,'//*[@id="__next"]/div/div[1]/main/div/div[2]/section/section')
    print(elems)
    termin = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/main/div/div[2]/section/section/div[2]/a/div[2]/div[1]/div/button')
    print(termin.text)
    
    # for elem in elems:
    #     termin = elem.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/main/div/div[2]/section/section/div[1]/a/div[2]/div[1]/div/div[3]/div[1]/div[1]')
    #     skad = elem.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/main/div/div[2]/section/section/div[1]/div[2]/a/div[2]/div[1]/div/div[3]/div[1]/div[2]')
    #     szama = elem.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/main/div/div[2]/section/section/div[1]/div[2]/a/div[2]/div[1]/div/div[3]/div[1]/div[3]')
    #     bp = elem.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/main/div/div[2]/section/section/div[1]/div[2]/a/div[2]/div[1]/div/div[3]/div[1]/div[4]')
    #     ocena = elem.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/main/div/div[2]/section/section/div[1]/div[2]/a/div[2]/div[2]/div/div[1]/div/div[1]/p')
    #     cena = elem.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/main/div/div[2]/section/section/div[1]/div[2]/a/div[2]/div[2]/div/div[2]/div/div[1]/h4/text()[1]')
    #     print(f"Termin {termin.text}, wylot z {skad.text}, rodzaj wyzywienia {szama.text}, biuro podróży: {bp.text}. Hotel ma ocene {ocena.text}, a wyjazd kosztuje {cena.text} za osoby!")
    #ActionChains.click(elem)
except Exception as e:
    print(f"Error: {str(e)}")
    
    
    
    #'//*[@id="__next"]/div/div[1]/main/div/div[2]/section/section/div[1]/div[2]/a/div[2]/div[1]/div/div[3]/div[1]/div[1]' #termin
    #'//*[@id="__next"]/div/div[1]/main/div/div[2]/section/section/div[1]/div[2]/a/div[2]/div[1]/div/div[3]/div[1]/div[2]' #skąd
    #'//*[@id="__next"]/div/div[1]/main/div/div[2]/section/section/div[1]/div[2]/a/div[2]/div[1]/div/div[3]/div[1]/div[3]' #rodzaj wyżywienia
    #'//*[@id="__next"]/div/div[1]/main/div/div[2]/section/section/div[1]/div[2]/a/div[2]/div[1]/div/div[3]/div[1]/div[4]' #bp
    
    #'//*[@id="__next"]/div/div[1]/main/div/div[2]/section/section/div[1]/div[2]/a/div[2]/div[2]/div/div[1]/div/div[1]/p' #ocena
    #'//*[@id="__next"]/div/div[1]/main/div/div[2]/section/section/div[1]/div[2]/a/div[2]/div[2]/div/div[2]/div/div[1]/h4/text()[1]' #cena