import pytest
from Locators import Locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

my_mail = "Daniil_Gorbachev_08_888@yandex.ru"
my_password = "123456"
@pytest.fixture()
def open_site():
    driver = webdriver.Chrome()
    driver.get(Locators.site_url)
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located(Locators.header_assemble_burger))
    yield driver
    driver.quit()


@pytest.fixture()
def authenticated_session(open_site):
    open_site.find_element(*Locators.enter_acc).click()
    WebDriverWait(open_site, 5).until(expected_conditions.presence_of_element_located(Locators.to_log_in_new))

    open_site.find_element(*Locators.email_field).send_keys(my_mail)
    open_site.find_element(*Locators.password_field).send_keys(my_password)
    open_site.find_element(*Locators.to_log_in_new).click()
    WebDriverWait(open_site, 5).until(expected_conditions.presence_of_element_located(Locators.place_order_new))
    return