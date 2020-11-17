import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

from PageObjects.CreateStatus import CreateStatus
from PageObjects.CreateWorkflow import CreateWorkflow
from PageObjects.LoginPage import Login
from Resources.successor import successor
from PageObjects.SuccessorAssign import SuccessorAssign
from Utilities.CustomLogger import LogGen
from Utilities.readProperties import Readconfig


@pytest.mark.successor
class Test_004_AssignSuccessor:
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

    def test_successor(self,setup):
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
        self.wf = CreateWorkflow(self.driver)
        time.sleep(3)
        self.wf.click_drop_down_menu()
        time.sleep(3)
        self.wf.select_admin_from_the_drop_down_menu()
        time.sleep(3)
        self.wf.click_breadcrumb_menu()
        time.sleep(3)
        self.wf.click_workflow_menu()
        time.sleep(3)
        self.wf.click_workflow_sub_menu()
        time.sleep(3)
        self.driver.get_screenshot_as_file(".\\Screenshoots\\workflow.png")
        self.assignstatus = CreateStatus(self.driver)
        self.assignstatus.search_workflow_name(self.workflow_name)
        time.sleep(3)
        self.assignstatus.select_workflow()
        time.sleep(3)
        self.logger.info("######## Assign successor to the created status ########")
        self.AS = SuccessorAssign(self.driver)
        self.AS.click_three_dot_icon_manager()
        time.sleep(1)
        self.AS.click_manager_successor_btn_three_dot_menu()
        time.sleep(2)
        self.logger.info("###### Assign successor1 to the Manager status ######")
        self.AS.click_create_new_successor_btn()
        time.sleep(2)
        self.AS.assign_successor_to_status("Back to originator")
        time.sleep(1)
        self.AS.assign_next_status_to_successor("Review by originator")
        time.sleep(1)
        self.AS.click_add_successor_btn()
        time.sleep(3)
        self.logger.info("###### Assign successor2 to the Manager status ######")
        self.AS.click_create_new_successor_btn()
        time.sleep(3)
        self.AS.assign_successor_to_status("Approve")
        time.sleep(3)
        self.AS.assign_next_status_to_successor("Approve")
        time.sleep(3)
        self.AS.click_add_successor_btn()
        time.sleep(3)
        self.logger.info("###### Assign successor3 to the Manager status ######")
        self.AS.click_create_new_successor_btn()
        time.sleep(3)
        self.AS.assign_successor_to_status("Reject")
        time.sleep(3)
        self.AS.assign_next_status_to_successor("Reject")
        time.sleep(3)
        self.AS.click_add_successor_btn()
        self.driver.get_screenshot_as_file(".\\Screenshoots\\successor1.png")
        time.sleep(3)
        self.AS.click_back_button()
        self.logger.info("###### Navigate back to status page ######")
        self.logger.info("###### Assign successor to the status Originator ######")
        time.sleep(3)
        self.AS.click_three_dot_icon_originator()
        time.sleep(3)
        self.AS.click_originator_successor_btn_three_dot_menu()
        time.sleep(3)
        self.AS.click_create_new_successor_btn()
        time.sleep(3)
        self.AS.assign_successor_to_status("Back to originator")
        time.sleep(3)
        self.AS.assign_next_status_to_successor("Review by manager")
        time.sleep(3)
        self.AS.click_add_successor_btn()
        time.sleep(2)
        self.driver.get_screenshot_as_file(".\\Screenshoots\\successor2.png")
        self.AS.click_back_button()
        time.sleep(2)














