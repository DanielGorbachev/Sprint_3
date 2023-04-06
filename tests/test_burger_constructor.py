from Locators import Locators


class TestBurgerConstructor:
    def test_section_switch_to_buns_buns_appears(self, open_site):
        element = open_site.find_element(*Locators.buns).get_attribute("class")
        assert "current" in element, "Не перешло на раздел 'Булки'"

    def test_section_switch_to_souses_souses_appears(self, open_site):
        open_site.find_element(*Locators.souses).click()
        element = open_site.find_element(*Locators.souses).get_attribute("class")
        assert "current" in element, "Не перешло на раздел 'Соусы'"

    def test_section_switch_to_stuffing_stuffing_appears(self, open_site):
        open_site.find_element(*Locators.stuffing).click()
        element = open_site.find_element(*Locators.stuffing).get_attribute("class")
        assert "current" in element, "Не перешло на раздел 'начинки'"