from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('chrome is up')
def step_impl(context):
   context.driver = webdriver.Chrome()
   context.driver.get("https://www3.animeflv.net/")

@when('the user get animeflv page')
def step_impl(context):

   context.driver.maximize_window()


@when('the user clics one piece')
def step_impl(context):
   link = context.driver.find_element(By.CSS_SELECTOR, "#mCSB_1_container > ul > li:nth-child(1) > a")
   link.click()


@then('the las episode is the 999')
def step_impl(context):
   numero = context.driver.find_element(By.CSS_SELECTOR, "#episodeList > li:nth-child(2) > a > p")
   assert numero.text == "Episodio 999"
   context.driver.quit()