from selenium.webdriver.common.by import By


# локаторы для страницы регистрации
class RegistrationLocators:
    NAME_FIELD = (By.XPATH, "//input[@name='name']")
    EMAIL_FIELD = (By.XPATH, "//fieldset[2]/div/div/input[@name='name']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")
    REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    ERROR_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")


# локаторы для страницы активации
class LoginLocators:
    LOGIN_FIELD = (By.XPATH, "//input[@name='name']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    RESET_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")


# локаторы для страницы восстановления пароля
class ResetPasswordLocators:
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")


# локаторы для главной страницы
class MianLocators:
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")
    SAUCES = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span')
    BUNS = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span')
    FILLINGS = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span')


# локаторы для страницы личного кабинета
class PersonalAccountLocators:
    PROFILE = (By.XPATH, "//a[text()='Профиль']")
    CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    LOGO = (By.XPATH, "//*[@id='root']/div/header/nav/div")
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")
