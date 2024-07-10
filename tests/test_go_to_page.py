from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import password, login
from locators import GoPageLocators


class TestGoToPage:
    def test_go_to_personal_account_from_main(self, driver):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*GoPageLocators.LOGIN_TO_ACCOUNT_BUTTON).click()

        driver.find_element(*GoPageLocators.LOGIN_FIELD).send_keys(login)
        driver.find_element(*GoPageLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*GoPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(GoPageLocators.ORDER_BUTTON))

        driver.find_element(*GoPageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(GoPageLocators.PROFILE))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
        driver.quit()

    def test_go_to_designer_from_personal_account_click_button(self, driver):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*GoPageLocators.LOGIN_TO_ACCOUNT_BUTTON).click()

        driver.find_element(*GoPageLocators.LOGIN_FIELD).send_keys(login)
        driver.find_element(*GoPageLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*GoPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(GoPageLocators.ORDER_BUTTON))

        driver.find_element(*GoPageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(GoPageLocators.PROFILE))

        driver.find_element(*GoPageLocators.CONSTRUCTOR).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(GoPageLocators.ORDER_BUTTON))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    def test_go_to_designer_from_personal_account_click_logo(self, driver):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*GoPageLocators.LOGIN_TO_ACCOUNT_BUTTON).click()

        driver.find_element(*GoPageLocators.LOGIN_FIELD).send_keys(login)
        driver.find_element(*GoPageLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*GoPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(GoPageLocators.ORDER_BUTTON))

        driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(GoPageLocators.PROFILE))

        driver.find_element(*GoPageLocators.LOGO).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(GoPageLocators.ORDER_BUTTON))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    def test_logout_in_personal_account_page(self, driver):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*GoPageLocators.LOGIN_TO_ACCOUNT_BUTTON).click()

        driver.find_element(*GoPageLocators.LOGIN_FIELD).send_keys(login)
        driver.find_element(*GoPageLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*GoPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(GoPageLocators.ORDER_BUTTON))

        driver.find_element(*GoPageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(GoPageLocators.PROFILE))

        driver.find_element(*GoPageLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(GoPageLocators.LOGIN_BUTTON))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()