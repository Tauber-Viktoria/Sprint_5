from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import password, login
from locators import LoginLocators, MianLocators, RegistrationLocators, ResetPasswordLocators


class TestLogin:
    @staticmethod
    def login(driver):
        driver.find_element(*LoginLocators.LOGIN_FIELD).send_keys(login)
        driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MianLocators.ORDER_BUTTON))

    def test_login_on_the_main_page(self, driver):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*MianLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
        self.login(driver)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    def test_login_through_personal_account(self, driver):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*MianLocators.PERSONAL_ACCOUNT).click()
        self.login(driver)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    def test_login_button_in_registration_form(self, driver):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*RegistrationLocators.LOGIN_LINK).click()
        self.login(driver)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    def test_login_button_in_password_recovery_form(self, driver):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*LoginLocators.RESET_PASSWORD_LINK).click()
        driver.find_element(*ResetPasswordLocators.LOGIN_LINK).click()
        self.login(driver)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()
