from selenium import webdriver
import pytest
@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    return driver