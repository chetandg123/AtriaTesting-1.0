from selenium import webdriver
import pytest
from selenium.webdriver.chrome import options

from utilities.ExcelUtils import reuseable


@pytest.fixture()
def setup():
    p = reuseable()
    driver = webdriver.Chrome(executable_path='/Driver')
    driver.implicitly_wait(30)
    return driver

