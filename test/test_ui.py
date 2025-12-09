import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import ver_film_name, ver_actor, neg_name
import allure


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title('Поиск фильма по названию')
@allure.description('Проверяется отображение названия фильма в шторке поиска')
@allure.feature('READ')
@allure.severity('critical')
@pytest.mark.ui
def test_search_film_name(driver):
    with allure.step('Открыть главную страницу сайта'):
        driver.get("https://www.kinopoisk.ru/")
    with allure.step('Ввести в поле поиска название фильма'):
        driver.find_element(By.NAME, "kp_query").send_keys(ver_film_name)
    with allure.step('Проверить в шторке поиска отображение названия фильма'):
        assert driver.find_element(
            By.ID, 'suggest-item-film-5148793'
            ).is_displayed()


@allure.title('Переход на страницу фильма')
@allure.description(
    'Проверяется отображение названия'
    r'фильма в заголовке на странице фильма'
)
@allure.feature('READ')
@allure.severity('normal')
@pytest.mark.ui
def test_film_page(driver):
    with allure.step('Открыть главную страницу сайта'):
        driver.get("https://www.kinopoisk.ru/")
    with allure.step('Ввести в поле поиска название фильма'):
        driver.find_element(By.NAME, "kp_query").send_keys(ver_film_name)
    with allure.step('Кликнуть по первому фильму в шторке поиска'):
        driver.find_element(By.ID, 'suggest-item-film-5148793').click()
    with allure.step('Проверить в заголовке страницы название фильма'):
        assert driver.find_element(
            By.CSS_SELECTOR, "span[data-tid='75209b22']"
            ).text == "Авиатор (2025)"


@allure.title('Поиск актера по имени')
@allure.description('Проверяется отображение имени актера в шторке поиска')
@allure.feature('READ')
@allure.severity('critical')
@pytest.mark.ui
def test_search_actor(driver):
    with allure.step('Открыть главную страницу сайта'):
        driver.get("https://www.kinopoisk.ru/")
    with allure.step('Ввести в поле поиска имя актера'):
        driver.find_element(By.NAME, "kp_query").send_keys(ver_actor)
    with allure.step('Проверить в шторке поиска отображение имени актера'):
        assert driver.find_element(
            By.ID, 'suggest-item-person-39984'
            ).is_displayed()


@allure.title('Переход на страницу актера')
@allure.description(
    'Проверяется отображение имени'
    r'актера в заголовке на странице актера'
)
@allure.feature('READ')
@allure.severity('normal')
@pytest.mark.ui
def test_actor_page(driver):
    with allure.step('Открыть главную страницу сайта'):
        driver.get("https://www.kinopoisk.ru/")
    with allure.step('Ввести в поле поиска имя актера'):
        driver.find_element(By.NAME, "kp_query").send_keys(ver_actor)
    with allure.step('Кликнуть по первому актеру в шторке поиска'):
        driver.find_element(By.ID, 'suggest-item-person-39984').click()
    with allure.step('Проверить в заголовке страницы имени актера'):
        assert driver.find_element(
            By.CLASS_NAME, "styles_primaryName__LB_CC"
            ).text == "Том Харди"


@allure.title('Поиск фильма по несуществующему имени')
@allure.description(
    'Проверяется отображение текста в шторке'
    r'поиска "По вашему запросу ничего не найдено"')
@allure.feature('READ')
@allure.severity('normal')
@pytest.mark.ui
def test_negativ_name(driver):
    with allure.step('Открыть главную страницу сайта'):
        driver.get("https://www.kinopoisk.ru/")
    with allure.step(
            'Ввести в поле поиска несуществующее'
            r'название фильма отображение текста'
            r'"По вашему запросу ничего не найдено"'
    ):
        driver.find_element(By.NAME, "kp_query").send_keys(neg_name)
    with allure.step('Проверить в в шторке поиска '):
        assert driver.find_element(
            By.CLASS_NAME, 'styles_emptySuggest__VnEa2'
            ).text == "По вашему запросу ничего не найдено"
