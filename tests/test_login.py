from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import password, login
from locators import LoginLocators, MainLocators, RegistrationLocators, ResetPasswordLocators


class TestLogin:

    def test_login_on_the_main_page(self, driver, login_in):
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_login_through_personal_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(*MainLocators.PERSONAL_ACCOUNT).click()
        driver.find_element(*LoginLocators.LOGIN_FIELD).send_keys(login)
        driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainLocators.ORDER_BUTTON))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_login_button_in_registration_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*RegistrationLocators.LOGIN_LINK).click()
        driver.find_element(*LoginLocators.LOGIN_FIELD).send_keys(login)
        driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainLocators.ORDER_BUTTON))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_login_button_in_password_recovery_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*LoginLocators.RESET_PASSWORD_LINK).click()
        driver.find_element(*ResetPasswordLocators.LOGIN_LINK).click()
        driver.find_element(*LoginLocators.LOGIN_FIELD).send_keys(login)
        driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainLocators.ORDER_BUTTON))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
