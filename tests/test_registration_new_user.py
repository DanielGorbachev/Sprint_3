from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locator import Locator
import random
import string


# генерация почты
def new_mail():
    mail_rand = f"Daniil_Gorbachev_08_{random.randint(100, 999)}@ya.ru"
    return mail_rand


# генерация пароля
def new_password():
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, 6))
    return rand_string


class TestRegistrationNewUser:
    def test_registration_new_user_positive_result(self, open_site):
        open_site.find_element(*Locator.cabinet).click()
        open_site.find_element(*Locator.to_register_href).click()
        open_site.find_element(*Locator.enter_name_field).send_keys("Даниил")
        open_site.find_element(*Locator.enter_mail_field).send_keys(new_mail())
        open_site.find_element(*Locator.password_field).send_keys(new_password())
        open_site.find_element(*Locator.to_register).click()
        WebDriverWait(open_site, 5).until(expected_conditions.visibility_of_element_located(
            Locator.header_enter))
        assert open_site.find_element(*Locator.to_log_in_new).text == "Войти"

    def test_registration_error_incorrect_password(self, open_site):
        open_site.find_element(*Locator.cabinet).click()
        open_site.find_element(*Locator.to_register_href).click()
        open_site.find_element(*Locator.enter_name_field).send_keys("Даниил")
        open_site.find_element(*Locator.enter_mail_field).send_keys(new_mail())
        open_site.find_element(*Locator.password_field).send_keys(new_password()[0:4])
        open_site.find_element(*Locator.to_register).click()
        assert open_site.find_element(*Locator.wrong_password).text == "Некорректный пароль"