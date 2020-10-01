import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chrome_path = "D:\\Request_App\\Drivers\\chromedriver.exe"
firefox_path = "D:\\Request_App\\Drivers\\geckodriver.exe"


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=".//Drivers//chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=".//Drivers//geckodriver.exe")
    elif browser == 'Ie':
        driver = webdriver.Ie()
    else:
        driver = webdriver.Chrome(executable_path=".//Drivers//chromedriver.exe")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")