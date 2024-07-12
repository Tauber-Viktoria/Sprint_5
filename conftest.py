import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import password, login
from locators import LoginLocators, MianLocators


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def login_in(driver):
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(*MianLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
    driver.find_element(*LoginLocators.LOGIN_FIELD).send_keys(login)
    driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(MianLocators.ORDER_BUTTON))
