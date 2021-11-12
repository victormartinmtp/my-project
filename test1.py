import time

import button as button
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from tkinter import *
from tkinter import messagebox as MessageBox

driver = webdriver.Chrome()

try:
    driver.get("https://www3.animeflv.net/")
    driver.maximize_window()
    time.sleep(5)
    text_box = driver.find_element(By.ID, "search-anime")
    text_box.send_keys("ousama king")
    boton = driver.find_element(By.CSS_SELECTOR, "body > div.Wrapper > header > div > div > div > div.AFixed > nav > div.Search > form > button")
    boton.click()
#    link_serie = driver.find_element(By.CSS_SELECTOR, "#mCSB_1_container > ul > li:nth-child(1) > a")
#    link_serie.click()
 #   link_ep = driver.find_element(By.CSS_SELECTOR, "#episodeList > li:nth-child(2) > a")
  #  print(link_ep.text)
   # assert link_ep.text == "Episodio 998"

finally:
    time.sleep(5)
    driver.quit()