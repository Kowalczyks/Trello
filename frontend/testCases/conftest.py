from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup(request):
    options = Options()
    options.add_argument('incognito')
    # add --headless to run in headless mode
    # driver = webdriver.Chrome(
    #      executable_path="C:\\Users\DKW\\PycharmProjects\\Trello\\frontend\\drivers\\chromedriver.exe", options=options)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    request.cls.driver = driver
    yield
    driver.quit()
