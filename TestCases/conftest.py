import os

from selenium import webdriver
import pytest
from selenium.webdriver.chrome import options

from get_directory import reuseable


@pytest.fixture()
def setup():

    p = reuseable()
    options = webdriver.ChromeOptions()
    prefs = {'download.default_directory':"/home/chetan/Downloads/Atria_Project/AtriaTesting-1.0/Downloads"}
    options.add_experimental_option('prefs', prefs)
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options, executable_path="/home/chetan/Downloads/Atria_Project/AtriaTesting-1.0/Driver/chromedriver")
    driver.implicitly_wait(30)
    return driver
