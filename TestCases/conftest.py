from selenium import webdriver
import pytest

from get_directory import DirectoryPath


@pytest.fixture()
def setup():
    path = DirectoryPath()
    options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': path.get_download_dir()}
    options.add_experimental_option('prefs', prefs)
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options, executable_path=path.get_driver_path())
    driver.implicitly_wait(30)
    return driver
