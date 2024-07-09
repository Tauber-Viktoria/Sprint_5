import pytest
from selenium.webdriver.chrome import webdriver


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()