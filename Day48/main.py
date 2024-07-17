from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value='cookie')


def purchase_item():
    available_products = ['Time machine', 'Portal', 'Alchemy lab', 'Shipment', 'Mine', 'Factory', 'Grandma', 'Cursor']
    for product in available_products:
        try:
            store_item = driver.find_element(By.XPATH, value =f'//*[@id="buy{product}"]/b')
            price = store_item.text.split('-')[1].strip().replace(',', '')
            cookies = driver.find_element(By.ID, value='money').text.replace(',', '')
            if int(cookies) > int(price):
                amount_to_buy = int(int(cookies)/int(price))
                for attempt in range(amount_to_buy):
                    try:
                        store_item.click()
                    except StaleElementReferenceException:
                        pass
                    except NoSuchElementException:
                        pass
        except StaleElementReferenceException:
            pass

baking = True
five_min = time.time() + 60*5
three_min = time.time() + 60*3
delay_interval = 5
purchase_delay = time.time() + delay_interval
next_milestone = three_min
while baking:
    if time.time() > five_min:
        cps = driver.find_element(By.ID, value='cps').text
        print(f"Final score: {cps}")
        break
    if time.time() >= purchase_delay:
            purchase_delay = time.time() + delay_interval
            purchase_item()
    if time.time() >= next_milestone:
        delay_interval += 5  # Increase purchase delay by 5 seconds
        next_milestone += 60
    cookie.click()