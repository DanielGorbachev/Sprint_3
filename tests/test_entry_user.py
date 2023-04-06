from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locator import Locator

my_mail = "Daniil_Gorbachev_08_888@yandex.ru"
my_password = "123456"


class TestUserLogIn:
    def test_login_from_main_page_positive_result(self, open_site):
        open_site.find_element(*Locator.enter_acc).click()
        open_site.find_element(*Locator.email_field).send_keys(my_mail)
        open_site.find_element(*Locator.password_field).send_keys(my_password)
        open_site.find_element(*Locator.to_log_in_new).click()
        WebDriverWait(open_site, 5).until(expected_conditions.presence_of_element_located(Locator.place_order_new))
        assert open_site.find_element(*Locator.place_order_new).text == "Оформить заказ"

    def test_login_from_personal_cabinet_positive_result(self, open_site):
        open_site.find_element(*Locator.cabinet).click()
        WebDriverWait(open_site, 5).until(expected_conditions.presence_of_element_located(Locator.to_log_in_new))
        open_site.find_element(*Locator.email_field).send_keys(my_mail)
        open_site.find_element(*Locator.password_field).send_keys(my_password)
        open_site.find_element(*Locator.to_log_in_new).click()
        WebDriverWait(open_site, 5).until(expected_conditions.presence_of_element_located(Locator.place_order_new))
        assert open_site.find_element(*Locator.place_order_new).text == "Оформить заказ"

    def test_login_from_registration_page_positive_result(self, open_site):
        open_site.find_element(*Locator.cabinet).click()
        open_site.find_element(*Locator.to_register_href).click()
        open_site.find_element(*Locator.to_login_href).click()
        open_site.find_element(*Locator.email_field).send_keys(my_mail)
        open_site.find_element(*Locator.password_field).send_keys(my_password)
        open_site.find_element(*Locator.to_log_in_new).click()
        WebDriverWait(open_site, 5).until(expected_conditions.presence_of_element_located(Locator.place_order_new))
        assert open_site.find_element(*Locator.place_order_new).text == "Оформить заказ"

    def test_login_from_password_recovery_page_positive_result(self, open_site):
        open_site.find_element(*Locator.enter_acc).click()
        WebDriverWait(open_site, 5).until(expected_conditions.presence_of_element_located(Locator.to_log_in_new))
        open_site.find_element(*Locator.recover_password).click()
        open_site.find_element(*Locator.to_login_href).click()
        open_site.find_element(*Locator.email_field).send_keys(my_mail)
        open_site.find_element(*Locator.password_field).send_keys(my_password)
        open_site.find_element(*Locator.to_log_in_new).click()
        WebDriverWait(open_site, 5).until(expected_conditions.presence_of_element_located(Locator.place_order_new))
        assert open_site.find_element(*Locator.place_order_new).text == "Оформить заказ"