from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import LoginLocators, MianLocators, PersonalAccountLocators


class TestGoToPage:
    def test_go_to_personal_account_from_main(self, driver, login_in):
        driver.find_element(*MianLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PersonalAccountLocators.PROFILE))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    def test_go_to_designer_from_personal_account_click_button(self, driver, login_in):
        driver.find_element(*MianLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PersonalAccountLocators.PROFILE))

        driver.find_element(*PersonalAccountLocators.CONSTRUCTOR).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MianLocators.ORDER_BUTTON))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_go_to_designer_from_personal_account_click_logo(self, driver, login_in):
        driver.find_element(*MianLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PersonalAccountLocators.PROFILE))

        driver.find_element(*PersonalAccountLocators.LOGO).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MianLocators.ORDER_BUTTON))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_logout_in_personal_account_page(self, driver, login_in):
        driver.find_element(*MianLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PersonalAccountLocators.PROFILE))

        driver.find_element(*PersonalAccountLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginLocators.LOGIN_BUTTON))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
