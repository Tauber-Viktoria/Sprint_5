import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

# Найди поле "Имя" и заполни его
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("some")

# Найди поле "Email" и заполни его
driver.find_element(By.XPATH, "//fieldset[2]/div/div/input[@name='name']").send_keys("some1234@mail.ru")


# Найди поле "Пароль" и заполни его
driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys("password")

# Найди кнопку "Зарегистрироваться" и кликни по ней
driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

# Добавь явное ожидание для загрузки страницы
time.sleep(3)

# Проверь, что текущий url равен 'https://qa-mesto.praktikum-services.ru/'
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

driver.quit()