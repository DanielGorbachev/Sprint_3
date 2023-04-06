from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locators import Locators

my_mail = "Daniil_Gorbachev_08_888@yandex.ru"
my_password = "123456"


class TestUserLogIn:
    def test_login_from_main_page_positive_result(self, open_site):
        open_site.find_element(*Locators.enter_acc).click()
        open_site.find_element(*Locators.email_field).send_keys(my_mail)
        open_site.find_element(*Locators.password_field).send_keys(my_password)
        open_site.find_element(*Locators.to_log_in_new).click()
        WebDriverWait(open_site, 5).until(expected_conditions.presence_of_element_located(Locators.place_order_new))
        assert open_site.find_element(*Locators.place_order_new).text == "Оформить заказ"

    def test_login_from_personal_cabinet_positive_result(self, open_site):
        open_site.find_element(*Locators.cabinet).click()
        WebDriverWait(open_site, 5).until(expected_conditions.presence_of_element_located(Locators.to_log_in_new))
        open_site.find_element(*Locators.email_field).send_keys(my_mail)
        open_site.find_element(*Locators.password_field).send_keys(my_password)
        open_site.find_element(*Locators.to_log_in_new).click()
        WebDriverWait(open_site, 5).until(expected_conditions.presence_of_element_located(Locators.place_order_new))
        assert open_site.find_element(*Locators.place_order_new).text == "Оформить заказ"

    def test_login_from_registration_page_positive_result(self, open_site):
        open_site.find_element(*Locators.cabinet).click()
        open_site.find_element(*Locators.to_register_href).click()
        open_site.find_element(*Locators.to_login_href).click()
        open_site.find_element(*Locators.email_field).send_keys(my_mail)
        open_site.find_element(*Locators.password_field).send_keys(my_password)
        open_site.find_element(*Locators.to_log_in_new).click()
        WebDriverWait(open_site, 5).until(expected_conditions.presence_of_element_located(Locators.place_order_new))
        assert open_site.find_element(*Locators.place_order_new).text == "Оформить заказ"

    def test_login_from_password_recovery_page_positive_result(self, open_site):
        open_site.find_element(*Locators.enter_acc).click()
        WebDriverWait(open_site, 5).until(expected_conditions.presence_of_element_located(Locators.to_log_in_new))
        open_site.find_element(*Locators.recover_password).click()
        open_site.find_element(*Locators.to_login_href).click()
        open_site.find_element(*Locators.email_field).send_keys(my_mail)
        open_site.find_element(*Locators.password_field).send_keys(my_password)
        open_site.find_element(*Locators.to_log_in_new).click()
        WebDriverWait(open_site, 5).until(expected_conditions.presence_of_element_located(Locators.place_order_new))
        assert open_site.find_element(*Locators.place_order_new).text == "Оформить заказ"