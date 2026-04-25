from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


options = webdriver.ChromeOptions()
options.add_argument("--headless")  

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


url = "https://coinmarketcap.com/"
driver.get(url)


time.sleep(5)


rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")

data = []

for row in rows[:10]:  
    try:
        name = row.find_element(By.CSS_SELECTOR, "p.sc-4984dd93-0").text
        price = row.find_element(By.CSS_SELECTOR, "div.sc-b3fc6b7-0").text
        
        data.append({
            "name": name,
            "price": price
        })
    except Exception as e:
        continue


for coin in data:
    print(f"{coin['name']}: {coin['price']}")


driver.quit()