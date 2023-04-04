from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Locators import Locators


class TestNavigationTabs:
    def test_open_tab_personal_cabinet_from_main_positive_result(self, authenticated_session):
        authenticated_session.find_element(*Locators.CABINET).click()
        WebDriverWait(authenticated_session, 10).until(expected_conditions.presence_of_element_located(
            Locators.MY_LOGIN_FIELD
        ))

        element = authenticated_session.find_element(By.XPATH, "//*[contains(text(), 'История заказов')]")
        assert element is not None

    def test_open_tab_konstruktor_from_personal_cabinet_positive_result(self, authenticated_session):
        authenticated_session.find_element(*Locators.CABINET).click()
        authenticated_session.find_element(By.XPATH, "//*[contains(text(), 'Конструктор')]").click()

        element = authenticated_session.find_element(By.XPATH, "//*[contains(text(), 'Соберите бургер')]")
        assert element is not None