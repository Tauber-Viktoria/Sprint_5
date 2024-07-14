
from locators import MainLocators


class TestSectionConstructor:

    def test_go_to_sections_buns(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*MainLocators.SAUCES).click()
        driver.find_element(*MainLocators.BUNS).click()

        buns_element = driver.find_element(*MainLocators.BUNS_ELEMENT)
        assert "current" in buns_element.get_attribute("class")

    def test_go_to_sections_sauces(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*MainLocators.SAUCES).click()

        sauces_element = driver.find_element(*MainLocators.SAUCES_ELEMENT)
        assert "current" in sauces_element.get_attribute("class")

    def test_go_to_sections_fillings(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*MainLocators.FILLINGS).click()

        fillings_element = driver.find_element(*MainLocators.FILLINGS_ELEMENT)
        assert "current" in fillings_element.get_attribute("class")
