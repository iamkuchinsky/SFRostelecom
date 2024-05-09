import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def web_driver(request):
    driver = webdriver.Chrome(executable_path='D:\chromedriver.exe')
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver
