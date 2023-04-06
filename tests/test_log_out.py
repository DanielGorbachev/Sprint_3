from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locators import Locators


class TestLogOut:
    def test_account_logging_out_positive_result(self, authenticated_session):
        authenticated_session.find_element(*Locators.cabinet).click()
        WebDriverWait(authenticated_session, 10).until(expected_conditions.presence_of_element_located(
            Locators.my_login_field_new
        ))
        authenticated_session.find_element(*Locators.exit_btn).click()
        WebDriverWait(authenticated_session, 10).until(expected_conditions.presence_of_element_located(
            Locators.to_log_in_new
        ))
        element = authenticated_session.find_element(*Locators.header_enter)
        assert element is not None