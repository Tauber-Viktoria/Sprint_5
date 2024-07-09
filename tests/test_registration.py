from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helper_tests import mail


class TestRegistration:
    def test_successful_registration(self, driver):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.XPATH, "//input[@name='name']").send_keys("some")
        driver.find_element(By.XPATH, "//fieldset[2]/div/div/input[@name='name']").send_keys(mail)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys("password")
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()

    def test_registration_password_error(self, driver):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.XPATH, "//input[@name='name']").send_keys("some")
        driver.find_element(By.XPATH, "//fieldset[2]/div/div/input[@name='name']").send_keys(mail)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys("pass")
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

        WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//p[text()='Некорректный пароль']")))

        assert driver.find_element(By.XPATH, "//p[text()='Некорректный пароль']")
        driver.quit()