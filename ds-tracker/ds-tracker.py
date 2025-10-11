from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


url = f'https://dexscreener.com/solana'


#Roadmapa tego projektu

# 1. Zrobić skanowanie top 10 assetów pod kątem wolumenu, mcap, mcap/wolumenu i wzrostów 1, 6, 24h
# 2. Wejść w asset, znaleźć top buyerów i dodać ich do listy

# 3. Top buyerów przerobić w innym scraperze i trackować na bieżąco transakcje
# 4. Ustawić to na live na jakimś renderze, przesyłać info po Discordzie, czy gdziekolwiek

# --- Research pompowanych coinów pod kątem wolumenu, retracementów, timingu i długości trwania poszczególnych akcji + takie rzeczy jak np. ataki na ATH - jak duże są to wybicia, jak często się udają, jak długo trwają z reguły, jak się nei udają, co temu towarzyszy ITD!
