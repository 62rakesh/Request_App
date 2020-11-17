import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from PageObjects.LoginPage import Login
from Testcases.conftest import setup
from PageObjects.CreateForm import CreateForm
from Utilities.readProperties import Readconfig
from Utilities.CustomLogger import LogGen


@pytest.mark.form
class Test_005_Form():
    base_url = Readconfig.getApplicationURL()
    username = Readconfig.getUsername()
    Password = Readconfig.getPassword()
    logger = LogGen.loggen()
    formname = Readconfig.getFormname()
    template_form_description = Readconfig.getFormdescription()

    def test_createform(self,setup):
        self.logger.info("###### Executing Test_004_AssignSuccessor test case ########")
        self.logger.info("############ Setting up with the login test execution ########### ")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.set_Username(self.username)
        time.sleep(1)
        self.lp.click_next_btn()
        time.sleep(2)
        self.lp.set_password(self.Password)
        time.sleep(1)
        self.lp.click_signin_btn()
        time.sleep(1)
        self.lp.click_confirm_btn()
        time.sleep(3)
        self.driver.get_screenshot_as_file(".\\Screenshoots\\login.png")
        self.logger.info("############ User is successfully logged in ########### ")
        print("Login is successfully completed")
        self.logger.info("###### Executing workflow script ######")
        self.form = CreateForm(self.driver)
        time.sleep(3)
        self.form.click_drop_down_menu()
        time.sleep(3)
        self.form.select_admin_from_the_drop_down_menu()
        time.sleep(3)
        self.form.click_breadcrumb_menu()
        time.sleep(3)
        self.form.click_form_management_menu()
        time.sleep(3)
        self.form.click_forms_button()
        time.sleep(3)
        self.form.click_add_form_button()
        time.sleep(2)
        self.form.enable_form_template_toggle()
        time.sleep(2)
        self.form.select_template_name("New hire")
        time.sleep(2)
        self.form.enter_form_name(self.formname)
        # self.driver.find_element_by_xpath("(//*[@id='name'])[2]").send_keys("RP-Starter form")
        time.sleep(2)
        # self.form.enter_descripton(self.template_form_description)
        # time.sleep(2)
        self.form.select_message_type("Hire")
        # select_message_type = Select(self.driver.find_element_by_xpath())
        time.sleep(3)
        self.form.add_request_form()
        time.sleep(5)


# form = Test_005_Form()
# form.test_createform(setup)
