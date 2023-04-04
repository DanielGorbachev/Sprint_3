import pytest
import random
import string
from Locators import Locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()       # открытие главной страницы сайты
def open_site():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, "html/body/div/div/header")))
    yield driver
    driver.quit()


@pytest.fixture()     # цикл входа на сайт
def authenticated_session(open_site, my_password, my_mail):
    open_site.find_element(*Locators.ENTER_ACC).click()
    WebDriverWait(open_site, 5).until(expected_conditions.presence_of_element_located(Locators.TO_LOG_IN))

    open_site.find_element(*Locators.EMAIL_FIELD).send_keys(my_mail)
    open_site.find_element(*Locators.PASSWORD_FIELD).send_keys(my_password)
    open_site.find_element(*Locators.TO_LOG_IN).click()
    WebDriverWait(open_site, 5).until(expected_conditions.presence_of_element_located(Locators.PLACE_ORDER))

    yield open_site

    open_site.quit()


@pytest.fixture      # генерация случайной почты
def new_mail():
    mail_rand = f"Daniil_Gorbachev_08_{random.randint(100, 999)}@ya.ru"
    return mail_rand


@pytest.fixture      # рандомный пароль из 6 символов
def new_password():
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, 6))
    return rand_string


@pytest.fixture    # мой логин
def my_mail():
    return "Daniil_Gorbachev_08_888@yandex.ru"


@pytest.fixture    # мой пароль
def my_password():
    return 123456