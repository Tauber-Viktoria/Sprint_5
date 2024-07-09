from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import password, login


class TestSectionConstructor:
    def test_go_to_sections_buns(self, driver):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

        driver.find_element(By.XPATH, "//input[@name='name']").send_keys(login)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span').click()
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span').click()

        driver.quit()

    def test_go_to_sections_sauces(self, driver):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

        driver.find_element(By.XPATH, "//input[@name='name']").send_keys(login)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span').click()

        driver.quit()

    def test_go_to_sections_fillings(self, driver):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

        driver.find_element(By.XPATH, "//input[@name='name']").send_keys(login)
        driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span').click()

        driver.quit()