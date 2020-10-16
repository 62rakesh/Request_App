from behave import given
from behave import when
from behave import then
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
base_url = "https://4d84732b-de61-4ed5-b3d6-2ef1ddc048b3.azurewebsites.net/"


@given('Launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get(base_url)
    context.driver.maximize_window()


@when('Open orange hrm homepage')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Open orange hrm homepage')


@then('Verify that the logo present on page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Verify that the logo present on page')


@then('close browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then close browser')

