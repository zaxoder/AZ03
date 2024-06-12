import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()

url = "https://www.divan.ru/category/divany-i-kresla"

driver.get(url)

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'lsooF'))
)

prices = driver.find_elements(By.CLASS_NAME, 'lsooF')

par_data = []

for card in prices:
    try:
        price = card.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU').text
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        continue

    par_data.append([price])

driver.quit()

with open("divan.csv", 'w', newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['Цена'])
    writer.writerows(par_data)