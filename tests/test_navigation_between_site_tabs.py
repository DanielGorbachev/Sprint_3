from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locator import Locator


class TestNavigationTabs:
    def test_open_tab_personal_cabinet_from_main_positive_result(self, authenticated_session):
        authenticated_session.find_element(*Locator.cabinet).click()
        WebDriverWait(authenticated_session, 10).until(expected_conditions.presence_of_element_located(
            Locator.my_login_field_new
        ))
        element = authenticated_session.find_element(*Locator.order_history_btn)
        assert element is not None

    def test_open_tab_konstruktor_from_personal_cabinet_positive_result(self, authenticated_session):
        authenticated_session.find_element(*Locator.cabinet).click()
        authenticated_session.find_element(*Locator.constructor_btn).click()
        element = authenticated_session.find_element(*Locator.header_assemble_burger)
        assert element is not None