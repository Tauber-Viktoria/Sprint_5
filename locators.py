from selenium.webdriver.common.by import By


# локаторы для регистрации
class RegistrationLocators:
    NAME_FIELD = (By.XPATH, "//input[@name='name']")
    EMAIL_FIELD = (By.XPATH, "//fieldset[2]/div/div/input[@name='name']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")
    REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    ERROR_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")


# локаторы для активации
class LoginLocators:
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    LOGIN_FIELD = (By.XPATH, "//input[@name='name']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")


