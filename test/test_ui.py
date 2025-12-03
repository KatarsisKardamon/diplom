from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.Page import MainPage

driver = webdriver.Chrome()
def test_authorization():
    user = MainPage(driver)
    user.open_main_page()
    my_phone = '501008094'
    user.authorization(my_phone)

def test_search():
    user = MainPage(driver)
    user.open_main_page()
    my_value = 'бесы'
    user.search(my_value)

def test_check():


sleep(4)
driver.quit()
