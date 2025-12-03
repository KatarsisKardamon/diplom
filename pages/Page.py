from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def open_main_page(self):
        self.driver.get("https://yandex.ru/")

        #self.driver.get("https://www.chitai-gorod.ru/")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def authorization(self, phone):
        self.phone = phone
        self.driver.find_element(
            By.CSS_SELECTOR, '[aria-label="Меню профиля"]').click()
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="phone"]').send_keys(self.phone)
        self.driver.find_element(
            By.CSS_SELECTOR, 'button.chg-app-button').click()

    def search(self, value):
        self.driver.find_element(
            By.CSS_SELECTOR, 'div.search-form__input-wrapper').send_keys({value})
        self.driver.find_element(
            By.CSS_SELECTOR, 'div.chg-app-button__content').click()

class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        self.driver.find_element(
            By.CSS_SELECTOR, 'button.chg-app-button').click()

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def in_cart(self):
        self.driver.find_element(
            By.CSS_SELECTOR, '[aria-label="Корзина"]').click()

    def check_cart(self):
        self.driver.find_element(
            By.CSS_SELECTOR, '').click()
        #class ="info-item__title" > 2 товара < / div >


    def order(self):
        self.driver.find_element(
            By.CSS_SELECTOR, '[mode="out-in"]').click()