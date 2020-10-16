import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.CreateStatus import CreateStatus
from PageObjects.CreateWorkflow import CreateWorkflow
from PageObjects.LoginPage import Login
from Testcases.create_workflow_test import Test_002_CreateWorkflow
from Resources.status import status
from Utilities.CustomLogger import LogGen
from Utilities.readProperties import Readconfig

# assignment_type = ['Manager', 'Originator', 'Position', 'Worker' ]
# fixed_value = ['Review', 'Approved', 'Rejected']


@pytest.mark.regression
class Test_003_StatusAssignment:
    base_url = Readconfig.getApplicationURL()
    username = Readconfig.getUsername()
    Password = Readconfig.getPassword()
    workflow_name = Readconfig.getWorkflowName()
    workflow_description = Readconfig.getDescription()
    status_name = Readconfig.getStatus1()
    status_name1 = Readconfig.getStatus2()
    status_name2 = Readconfig.getStatus3()
    status_name3 = Readconfig.getStatus4()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_statusassignment(self, setup):
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
        self.driver.get_screenshot_as_file(".\\Screenshoots\\workflow.png")
        self.logger.info("####### Workflow is created successfuly ########")
        self.assignstatus = CreateStatus(self.driver)
        self.assignstatus.search_workflow_name(self.workflow_name)
        time.sleep(3)
        self.assignstatus.select_workflow()
        time.sleep(1)
        self.logger.info("####### Assign status in the workflow ########")
        self.assignstatus.click_add_new_status_btn()
        time.sleep(1)
        self.assignstatus.enter_status(self.status_name)
        time.sleep(1)
        self.logger.info("####### Executing Test_003_StatusAssignment test case for status assignment")
        self.logger.info("####### Assigning manager status1 to the workflow ########")
        self.assignstatus.select_assign_type("Manager")
        time.sleep(2)
        # self.assignstatus.select_fixed_value("Review")
        # time.sleep(2)
        self.assignstatus.enable_assignee_toggle()
        time.sleep(1)
        self.assignstatus.enable_originator_toggle()
        time.sleep(1)
        self.assignstatus.add_status()
        self.driver.get_screenshot_as_file(".\\Screenshoots\\.png")
        time.sleep(3)
        self.logger.info("####### Assigning originator status2 to the workflow ########")
        self.assignstatus.click_add_new_status_btn()
        time.sleep(1)
        self.assignstatus.enter_status(self.status_name1)
        time.sleep(1)
        self.assignstatus.select_assign_type("Originator")
        time.sleep(2)
        self.assignstatus.select_fixed_value("Review")
        time.sleep(2)
        self.assignstatus.enable_assignee_toggle()
        time.sleep(1)
        self.assignstatus.enable_originator_toggle()
        time.sleep(1)
        self.assignstatus.add_status()
        self.driver.get_screenshot_as_file(".\\Screenshots\\status_originator.png")
        time.sleep(3)
        self.logger.info("####### Assigning manager status3 to the workflow ########")
        self.assignstatus.click_add_new_status_btn()
        time.sleep(1)
        self.assignstatus.enter_status(self.status_name2)
        time.sleep(1)
        self.assignstatus.select_assign_type("Manager")
        time.sleep(2)
        self.assignstatus.select_fixed_value("End approved")
        time.sleep(2)
        self.assignstatus.enable_assignee_toggle()
        time.sleep(1)
        self.assignstatus.enable_originator_toggle()
        time.sleep(1)
        self.assignstatus.add_status()
        self.driver.get_screenshot_as_file(".\\Screenshots\\manager2.png")
        time.sleep(3)
        self.logger.info("####### Assigning manager status4 to the workflow ########")
        self.assignstatus.click_add_new_status_btn()
        time.sleep(1)
        self.assignstatus.enter_status(self.status_name3)
        time.sleep(1)
        self.assignstatus.select_assign_type("Manager")
        time.sleep(2)
        self.assignstatus.select_fixed_value("End rejected")
        time.sleep(2)
        self.assignstatus.enable_assignee_toggle()
        time.sleep(1)
        self.assignstatus.enable_originator_toggle()
        time.sleep(1)
        self.assignstatus.add_status()
        self.driver.get_screenshot_as_file(".\\Screenshots\\manager3.png")
        time.sleep(3)
        self.driver.get_screenshot_as_file(".\\Screenshots\\assigned_status.png")
















