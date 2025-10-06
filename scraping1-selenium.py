from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


url = 'https://www.filmweb.pl/ranking/premiere'



#starting a new session
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.get(url = 'https://www.filmweb.pl/ranking/premiere')

#skipping the cookie button
clickable = driver.find_element(By.XPATH, '//*[@id="didomi-notice-agree-button"]')
try:
    time.sleep(3)
    clickable.click()
except Exception as e:
    print(f"Error: {str(e)}")


#skipping the ad with the Continue to Filmweb button (it shows up inconsistently)
try:
    
    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "__tcfapiLocator")))
    elems = driver.find_element(By.XPATH, '//*[@id="site"]/div[6]/div/div/div[3]/section[1]/div[3]')
    print (elems)
except Exception as e:
    print(f'Error: {str(e)}')

#fetching the list of top 10 movies (tbd)