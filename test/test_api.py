import requests
from config import TOKEN, base_url, ver_film_name, ver_actor, ver_year, ver_fees_russia_value, neg_ver_year
import allure


HEADERS = {"X-API-KEY": TOKEN}


@allure.title('Поиск фильма по названию')
@allure.description('Проверяется статус-код 200')
@allure.feature('READ')
@allure.severity('critical')
def test_search_film_name_api():
    with allure.step('Задать url запроса'):
        url = f"{base_url}/v1.4/movie/search"
    with allure.step('Задать параметры запроса с переменной ver_film_name'):
        params = {
            "page": 1,
            "limit": 10,
            "query": ver_film_name
        }
    with allure.step('Передать GET запрос'):
        resp = requests.get(url, headers=HEADERS, params=params)
    with allure.step('Проверить статус-код'):
        assert resp.status_code == 200


@allure.title('Поиск актера по имени')
@allure.description('Проверяется статус-код 200')
@allure.feature('READ')
@allure.severity('critical')
def test_search_actor_api():
    with allure.step('Задать url запроса'):
        url = f"{base_url}/v1.4/person/search"
    with allure.step('Задать параметры запроса с переменной ver_actor'):
        params = {
            "page": 1,
            "limit": 10,
            "query": ver_actor
        }
    with allure.step('Передать GET запрос'):
        resp = requests.get(url, headers=HEADERS, params=params)
    with allure.step('Проверить статус-код'):
        assert resp.status_code == 200


@allure.title('Поиск фильма по фильтрам')
@allure.description('Проверяется статус-код 200')
@allure.feature('READ')
@allure.severity('normal')
def test_search_random_api():
    with allure.step('Задать url запроса'):
        url = f"{base_url}/v1.4/movie/random"
    with allure.step('Задать параметры запроса с переменными ver_year, ver_fees_russia_value'):
        params = {
            "notNullFields": 'year',
            "year": ver_year,
            "fees.russia.value": ver_fees_russia_value
        }
    with allure.step('Передать GET запрос'):
        resp = requests.get(url, headers=HEADERS, params=params)
    with allure.step('Проверить статус-код'):
        assert resp.status_code == 200


@allure.title('Поиск фильма по фильтрам (негативный)')
@allure.description('Проверяется статус-код 400')
@allure.feature('READ')
@allure.severity('normal')
def test_negativ_search_random_api():
    with allure.step('Задать url запроса'):
        url = f"{base_url}/v1.4/movie/random"
    with allure.step('Задать параметры запроса с переменными neg_ver_year, ver_fees_russia_value'):
        params = {
            "notNullFields": 'year',
            "year": neg_ver_year,
            "fees.russia.value": ver_fees_russia_value
        }
    with allure.step('Передать GET запрос'):
        resp = requests.get(url, headers=HEADERS, params=params)
    with allure.step('Проверить статус-код'):
        assert resp.status_code == 400


@allure.title('Поиск актекра по имени (негативный)')
@allure.description('Проверяется статус-код 401')
@allure.feature('READ')
@allure.severity('normal')
def test_negativ_search_actor_api():
    with allure.step('Задать url запроса'):
        url = f"{base_url}/v1.4/person/search"
    with allure.step('Задать параметры запроса с переменными ver_actor'):
        params = {
            "page": 1,
            "limit": 10,
            "query": ver_actor
        }
    with allure.step('Передать GET запрос без Headers'):
        resp = requests.get(url, params=params)
    with allure.step('Проверить статус-код'):
        assert resp.status_code == 401
