from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import password, login
from locators import ConstructorLocators


class TestSectionConstructor:
    def test_go_to_sections_buns(self, driver):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*ConstructorLocators.PERSONAL_ACCOUNT).click()

        driver.find_element(*ConstructorLocators.LOGIN_FIELD).send_keys(login)
        driver.find_element(*ConstructorLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*ConstructorLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(ConstructorLocators.ORDER_BUTTON))

        driver.find_element(*ConstructorLocators.SAUCES).click()
        driver.find_element(*ConstructorLocators.BUNS).click()

        driver.quit()

    def test_go_to_sections_sauces(self, driver):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*ConstructorLocators.PERSONAL_ACCOUNT).click()

        driver.find_element(*ConstructorLocators.LOGIN_FIELD).send_keys(login)
        driver.find_element(*ConstructorLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*ConstructorLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(ConstructorLocators.ORDER_BUTTON))

        driver.find_element(*ConstructorLocators.SAUCES).click()

        driver.quit()

    def test_go_to_sections_fillings(self, driver):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*ConstructorLocators.PERSONAL_ACCOUNT).click()

        driver.find_element(*ConstructorLocators.LOGIN_FIELD).send_keys(login)
        driver.find_element(*ConstructorLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*ConstructorLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(ConstructorLocators.ORDER_BUTTON))

        driver.find_element(*ConstructorLocators.FILLINGS).click()

        driver.quit()
