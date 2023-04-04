from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locators import Locators


class TestRegistrationNewUser:
    def test_registration_new_user_positive_result(self, open_site, new_mail, new_password):
        open_site.find_element(*Locators.CABINET).click()
        open_site.find_element(*Locators.TO_REGISTER).click()

        open_site.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("Даниил")
        open_site.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(new_mail)
        open_site.find_element(By.XPATH, ".//fieldset[3]/div/div/input").send_keys(new_password)

        open_site.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()

        WebDriverWait(open_site, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "/html/body/div[1]/div/main/div/h2[text()='Вход']")))

        assert open_site.find_element(*Locators.TO_LOG_IN).text == "Войти"

    def test_registration_error_incorrect_password(self, open_site, new_mail, new_password):
        open_site.find_element(*Locators.CABINET).click()
        open_site.find_element(*Locators.TO_REGISTER).click()

        open_site.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("Даниил")
        open_site.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(new_mail)
        # Минимальный пароль — шесть символов, вводим 5
        open_site.find_element(By.XPATH, ".//fieldset[3]/div/div/input").send_keys(new_password[0:4])
        open_site.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()

        assert open_site.find_element(By.CSS_SELECTOR, ".input__error").text == "Некорректный пароль"
