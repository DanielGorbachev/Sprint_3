from Locator import Locator


class TestBurgerConstructor:
    def test_section_switch_to_buns_buns_appears(self, open_site):
        element = open_site.find_element(*Locator.buns).get_attribute("class")
        assert "current" in element, "Не перешло на раздел 'Булки'"

    def test_section_switch_to_souses_souses_appears(self, open_site):
        open_site.find_element(*Locator.souses).click()
        element = open_site.find_element(*Locator.souses).get_attribute("class")
        assert "current" in element, "Не перешло на раздел 'Соусы'"

    def test_section_switch_to_stuffing_stuffing_appears(self, open_site):
        open_site.find_element(*Locator.stuffing).click()
        element = open_site.find_element(*Locator.stuffing).get_attribute("class")
        assert "current" in element, "Не перешло на раздел 'начинки'"