import time

import button as button
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/tables")
    driver.maximize_window()
    fila1 = driver.find_element(By.CSS_SELECTOR, "#table1 > tbody > tr:nth-child(1)")
    fila2 = driver.find_element(By.CSS_SELECTOR, "#table1 > tbody > tr:nth-child(2)")
    filas = fila1 + fila2

    for fila in filas:
        fila
finally:

    time.sleep(1)