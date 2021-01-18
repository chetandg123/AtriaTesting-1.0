import os

from selenium import webdriver
import pytest
from selenium.webdriver.chrome import options

from utilities.ExcelUtils import reuseable


@pytest.fixture()
def setup():
    p = reuseable()
    driver = webdriver.Chrome(executable_path="/home/chetan/Downloads/Atria_Project/AtriaTesting-1.0/Driver/chromedriver")
    driver.implicitly_wait(30)
    return driver

    # options = webdriver.ChromeOptions()
    # prefs = {'download.default_directory': p.get_download_dir()}
    # options.add_experimental_option('prefs', prefs)
    # # options.add_argument('--headless')
    # driver = webdriver.Chrome(options=options, executable_path=p.get_driver_path())
    # return driver
