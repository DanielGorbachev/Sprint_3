from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locator import Locator


class TestLogOut:
    def test_account_logging_out_positive_result(self, authenticated_session):
        authenticated_session.find_element(*Locator.cabinet).click()
        WebDriverWait(authenticated_session, 10).until(expected_conditions.presence_of_element_located(
            Locator.my_login_field_new
        ))
        authenticated_session.find_element(*Locator.exit_btn).click()
        WebDriverWait(authenticated_session, 10).until(expected_conditions.presence_of_element_located(
            Locator.to_log_in_new
        ))
        element = authenticated_session.find_element(*Locator.header_enter)
        assert element is not None