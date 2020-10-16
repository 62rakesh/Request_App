import time
import pytest
from selenium import webdriver
from pytest import mark
from selenium import webdriver

from PageObjects.CreateStatus import CreateStatus
from PageObjects.LoginPage import Login
from PageObjects.CreateWorkflow import CreateWorkflow
from Testcases.login_test import Test_001_Login
from Utilities.CustomLogger import LogGen
from Utilities.readProperties import Readconfig


@pytest.mark.regression
class Test_002_CreateWorkflow:
    base_url = Readconfig.getApplicationURL()
    username = Readconfig.getUsername()
    Password = Readconfig.getPassword()
    workflow_name = Readconfig.getWorkflowName()
    workflow_description = Readconfig.getDescription()
    status_name = Readconfig.getStatus1()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_createworkflow(self, setup):
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
        self.logger.info("######### Creating WorkFlow #########")
        self.wf=CreateWorkflow(self.driver)
        time.sleep(1)
        self.wf.click_drop_down_menu()
        time.sleep(1)
        self.wf.select_admin_from_the_drop_down_menu()
        time.sleep(1)
        self.wf.click_breadcrumb_menu()
        time.sleep(1)
        self.wf.click_workflow_menu()
        time.sleep(1)
        self.wf.click_workflow_sub_menu()
        time.sleep(1)
        self.wf.click_new_button()
        time.sleep(2)
        self.wf.enter_workflow_name(self.workflow_name)
        time.sleep(1)
        self.wf.enter_workflow_description(self.workflow_description)
        time.sleep(1)
        self.wf.active_toggle()
        time.sleep(1)
        self.wf.add_workflow()
        time.sleep(3)
        self.logger.info("####### Workflow is created successfuly ########")
        # self.assignstatus = CreateStatus(self.driver)
        # self.assignstatus.search_workflow_name(self.workflow_name)
        # time.sleep(1)
        # self.assignstatus.select_workflow()
        # time.sleep(1)
        # self.assignstatus.click_add_status_btn()
        # time.sleep(1)
        # self.assignstatus.enter_status(self.status_name)
        # time.sleep(1)
