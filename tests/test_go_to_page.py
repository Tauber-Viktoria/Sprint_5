from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import password, login


class TestGoToPage:
    def test_go_to_personal_account_from_main(self, driver):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

        driver.find_element(By.XPATH, "//input[@name='name']").send_keys(login)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

        driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//a[text()='Профиль']")))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
        driver.quit()

    def test_go_to_designer_from_personal_account_click_button(self, driver):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

        driver.find_element(By.XPATH, "//input[@name='name']").send_keys(login)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

        driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//a[text()='Профиль']")))
        driver.find_element(By.XPATH, "//p[text()='Конструктор']").click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    def test_go_to_designer_from_personal_account_click_logo(self, driver):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

        driver.find_element(By.XPATH, "//input[@name='name']").send_keys(login)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

        driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//a[text()='Профиль']")))
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/div').click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    def test_logout_in_personal_account_page(self, driver):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

        driver.find_element(By.XPATH, "//input[@name='name']").send_keys(login)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

        driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//a[text()='Профиль']")))
        driver.find_element(By.XPATH, "//button[text()='Выход']").click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()