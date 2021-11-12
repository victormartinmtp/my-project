import time

import button as button
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from tkinter import *
from tkinter import messagebox as MessageBox

driver = webdriver.Chrome()


def marcar_check(check1, check2):
        try:
            ck1 = driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(1)")
            ck2 = driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(3)")
            if check1:
                if not ck1.is_selected():
                    ck1.click()
            else:
                if ck1.is_selected():
                    ck1.click()
            if check2:
                if not ck2.is_selected():
                    ck2.click()
            else:
                if ck2.is_selected():
                    ck2.click()
        finally:
            time.sleep(1)

driver.get("https://the-internet.herokuapp.com/checkboxes")
marcar_check(True, True)
time.sleep(1)
marcar_check(False, False)
time.sleep(1)
marcar_check(True, False)
time.sleep(1)
marcar_check(False, True)
time.sleep(1)