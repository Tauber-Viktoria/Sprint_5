from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helper_tests import RandomMail
from locators import RegistrationLocators, LoginLocators


class TestRegistration:
    def test_successful_registration(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        email = RandomMail.generate_mail()
        driver.find_element(*RegistrationLocators.NAME_FIELD).send_keys("some")
        driver.find_element(*RegistrationLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*RegistrationLocators.PASSWORD_FIELD).send_keys("password")
        driver.find_element(*RegistrationLocators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginLocators.LOGIN_BUTTON))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_registration_password_error(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        email = RandomMail.generate_mail()
        driver.find_element(*RegistrationLocators.NAME_FIELD).send_keys("some")
        driver.find_element(*RegistrationLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*RegistrationLocators.PASSWORD_FIELD).send_keys("pass")
        driver.find_element(*RegistrationLocators.REGISTRATION_BUTTON).click()

        error_message = WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located(RegistrationLocators.ERROR_MESSAGE))

        assert error_message.text == 'Некорректный пароль'