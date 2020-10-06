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
    yield driver
    driver.close()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# Generate HTMl report


def pytest_configure(config):

    config._metadata['Project Name'] = 'HR_Request'
    config._metadata['Customers Name'] = 'Fourvision'
    config._metadata['Testers Name'] = 'Rakesh Patra'
    config._metadata['Sprint'] ='2.11'
    config._metadata['Testcases type'] = 'Regression'
    config._metadata['Date of execution'] = '05-10-2020'


# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)

