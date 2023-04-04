from Locators import Locators


class TestBurgerConstructor:
    def test_section_switch_to_buns_buns_appears(self, open_site):
        element = open_site.find_element(*Locators.BUNS).get_attribute("class")
        assert "current" in element

    def test_section_switch_to_souses_souses_appears(self, open_site):
        open_site.find_element(*Locators.SOUSES).click()
        element = open_site.find_element(*Locators.SOUSES).get_attribute("class")
        assert "current" in element

    def test_section_switch_to_stuffing_stuffing_appears(self, open_site):
        open_site.find_element(*Locators.STUFFING).click()
        element = open_site.find_element(*Locators.STUFFING).get_attribute("class")
        assert "current" in element