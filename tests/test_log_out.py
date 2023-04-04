from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locators import Locators


class TestLogOut:
    def test_account_logging_out_positive_result(self, authenticated_session):
        authenticated_session.find_element(*Locators.CABINET).click()
        WebDriverWait(authenticated_session, 10).until(expected_conditions.presence_of_element_located(
            Locators.MY_LOGIN_FIELD
        ))
        authenticated_session.find_element(By.XPATH, "//button[contains(text(),'Выход')]").click()
        WebDriverWait(authenticated_session, 10).until(expected_conditions.presence_of_element_located(
            Locators.TO_LOG_IN
        ))
        element = authenticated_session.find_element(By.XPATH, "//h2[contains(text(),'Вход')]")
        assert element is not None
