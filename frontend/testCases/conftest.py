from backend.helpers.api_board import APIBoard
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup():
    options = Options()
    options.add_argument('incognito')
    # add --headless to run in headless mode
    # driver = webdriver.Chrome(
    #     executable_path="..frontend\\drivers\\chromedriver.exe", options=options)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    return driver
