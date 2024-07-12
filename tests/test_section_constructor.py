from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import MianLocators


class TestSectionConstructor:

    def test_go_to_sections_buns(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*MianLocators.SAUCES).click()
        driver.find_element(*MianLocators.BUNS).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MianLocators.BUNS_ELEMENT))

        assert driver.find_element(*MianLocators.BUNS_ELEMENT)

    def test_go_to_sections_sauces(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*MianLocators.SAUCES).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MianLocators.SAUCES_ELEMENT))

        assert driver.find_element(*MianLocators.SAUCES_ELEMENT)

    def test_go_to_sections_fillings(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*MianLocators.FILLINGS).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MianLocators.FILLINGS_ELEMENT))

        assert driver.find_element(*MianLocators.FILLINGS_ELEMENT)
