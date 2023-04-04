from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locators import Locators


class TestUserLogIn:
    def test_login_from_main_page_positive_result(self, open_site, my_mail, my_password):
        open_site.find_element(*Locators.ENTER_ACC).click()
        # WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(Locators.TO_LOG_IN))

        open_site.find_element(*Locators.EMAIL_FIELD).send_keys(my_mail)
        open_site.find_element(*Locators.PASSWORD_FIELD).send_keys(my_password)
        open_site.find_element(*Locators.TO_LOG_IN).click()
        WebDriverWait(open_site, 5).until(expected_conditions.presence_of_element_located(Locators.PLACE_ORDER))

        assert open_site.find_element(*Locators.PLACE_ORDER).text == "Оформить заказ"

    def test_login_from_personal_cabinet_positive_result(self, open_site, my_mail, my_password):
        open_site.find_element(*Locators.CABINET).click()
        WebDriverWait(open_site, 5).until(expected_conditions.presence_of_element_located(Locators.TO_LOG_IN))

        open_site.find_element(*Locators.EMAIL_FIELD).send_keys(my_mail)
        open_site.find_element(*Locators.PASSWORD_FIELD).send_keys(my_password)
        open_site.find_element(*Locators.TO_LOG_IN).click()
        WebDriverWait(open_site, 5).until(expected_conditions.presence_of_element_located(Locators.PLACE_ORDER))

        assert open_site.find_element(*Locators.PLACE_ORDER).text == "Оформить заказ"

    def test_login_from_registration_page_positive_result(self, open_site, my_mail, my_password):
        open_site.find_element(*Locators.CABINET).click()
        open_site.find_element(*Locators.TO_REGISTER).click()
        open_site.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()

        open_site.find_element(*Locators.EMAIL_FIELD).send_keys(my_mail)
        open_site.find_element(*Locators.PASSWORD_FIELD).send_keys(my_password)
        open_site.find_element(*Locators.TO_LOG_IN).click()
        WebDriverWait(open_site, 5).until(expected_conditions.presence_of_element_located(Locators.PLACE_ORDER))

        assert open_site.find_element(*Locators.PLACE_ORDER).text == "Оформить заказ"

    def test_login_from_password_recovery_page_positive_result(self, open_site, my_mail, my_password):
        open_site.find_element(*Locators.ENTER_ACC).click()
        WebDriverWait(open_site, 5).until(expected_conditions.presence_of_element_located(Locators.TO_LOG_IN))

        open_site.find_element(By.XPATH, "//a[contains(text(),'Восстановить пароль')]").click()
        open_site.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()

        open_site.find_element(*Locators.EMAIL_FIELD).send_keys(my_mail)
        open_site.find_element(*Locators.PASSWORD_FIELD).send_keys(my_password)
        open_site.find_element(*Locators.TO_LOG_IN).click()
        WebDriverWait(open_site, 5).until(expected_conditions.presence_of_element_located(Locators.PLACE_ORDER))

        assert open_site.find_element(*Locators.PLACE_ORDER).text == "Оформить заказ"