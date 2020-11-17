import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.CreateForm import CreateForm
from PageObjects.LoginPage import Login
from Utilities.CustomLogger import LogGen
from Utilities.readProperties import Readconfig
from PageObjects.request_group import RequestGroup


@pytest.mark.group
class Test_006_Group():
    base_url = Readconfig.getApplicationURL()
    username = Readconfig.getUsername()
    Password = Readconfig.getPassword()
    logger = LogGen.loggen()
    request_group = Readconfig.getRequestgroupname()
    group_description = Readconfig.getGroupdescription()
    RequestType = Readconfig.getRequestTypename()
    RequestType_Description = Readconfig.getRequestTypeDescription()
    workflow_name = Readconfig.getWorkflowName()
    form_name = Readconfig.getFormname()

    def test_creategroup(self,setup):
        self.logger.info("###### Executing Test_004_AssignSuccessor test case ########")
        self.logger.info("############ Setting up with the login test execution ########### ")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.base_url)
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(2)
        self.lp = Login(self.driver)
        time.sleep(2)
        self.lp.set_Username(self.username)
        time.sleep(2)
        self.lp.click_next_btn()
        time.sleep(2)
        self.lp.set_password(self.Password)
        time.sleep(2)
        self.lp.click_signin_btn()
        time.sleep(2)
        self.lp.click_confirm_btn()
        time.sleep(2)
        self.driver.get_screenshot_as_file(".\\Screenshoots\\login.png")
        self.logger.info("############ User is successfully logged in ########### ")
        print("Login is successfully completed")
        self.logger.info("###### Executing workflow script ######")
        self.form = CreateForm(self.driver)
        time.sleep(2)
        self.form.click_drop_down_menu()
        time.sleep(2)
        self.form.select_admin_from_the_drop_down_menu()
        time.sleep(2)
        self.form.click_breadcrumb_menu()
        time.sleep(2)
        self.RG=RequestGroup(self.driver)
        self.logger.info("######## Working on the request group creation ########")
        self.RG.click_request_group()
        time.sleep(2)
        self.RG.create_a_new_request_group()
        time.sleep(2)
        self.RG.enter_request_group_name(self.request_group)
        time.sleep(2)
        self.RG.enter_request_group_description(self.group_description)
        time.sleep(2)
        self.RG.click_enable_active_toggle()
        time.sleep(2)
        self.RG.click_add_button()
        time.sleep(2)
        self.logger.info("######## The request group is added successfully ########")
        self.RG.search_request_group_name(self.request_group)
        time.sleep(3)
        self.RG.click_selected_request_group_name()
        time.sleep(3)
        self.RG.create_a_new_request_type()
        time.sleep(3)
        self.RG.enter_request_type_name(self.RequestType)
        time.sleep(2)
        self.RG.add_request_type_description(self.RequestType_Description)
        time.sleep(3)
        self.RG.select_workflow(self.workflow_name)
        time.sleep(3)
        self.RG.select_request_form(self.form_name)
        time.sleep(3)
        self.RG.add_request_type()
        time.sleep(5)
        self.logger.info("######## A new request type is created successfully #########")





