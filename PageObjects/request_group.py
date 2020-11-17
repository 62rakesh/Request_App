from selenium import webdriver
from PageObjects.CreateWorkflow import CreateWorkflow
from Resources.requestgroup_locator import Group
from selenium.webdriver.support.select import Select
from Utilities.readProperties import Readconfig


class RequestGroup(Group, CreateWorkflow, Readconfig):
    def __init__(self, driver):
        super().__init__(driver)

    def click_request_group(self):
        self.driver.find_element_by_xpath(self.request_group_xpath).click()

    def create_a_new_request_group(self):
        self.driver.find_element_by_xpath(self.create_new_request_group_xpath).click()

    def enter_request_group_name(self, group_name):
        self.driver.find_element_by_xpath(self.enter_name_xpath).clear()
        self.driver.find_element_by_xpath(self.enter_name_xpath).send_keys(group_name)

    def enter_request_group_description(self, group_description):
        self.driver.find_element_by_xpath(self.enter_description_xpath).clear()
        self.driver.find_element_by_xpath(self.enter_description_xpath).send_keys(group_description)

    def click_enable_active_toggle(self):
        self.driver.find_element_by_xpath(self.enable_toggle_xpath).click()

    def click_add_button(self):
        self.driver.find_element_by_xpath(self.add_request_group_xpath).click()

    def search_request_group_name(self, request_group_name):
        self.driver.find_element_by_xpath(self.search_group_xpath).clear()
        self.driver.find_element_by_xpath(self.search_group_xpath).send_keys(request_group_name)

    def click_selected_request_group_name(self):
        self.driver.find_element_by_xpath(self.find_group_name_xpath).click()

    def create_a_new_request_type(self):
        self.driver.find_element_by_xpath(self.create_new_request_type_xpath).click()

    def enter_request_type_name(self, request_type):
        self.driver.find_element_by_xpath(self.enter_request_type_name_xpath).clear()
        self.driver.find_element_by_xpath(self.enter_request_type_name_xpath).send_keys(request_type)

    def add_request_type_description(self, request_type_description):
        self.driver.find_element_by_xpath(self.enter_request_type_description_xpath).clear()
        self.driver.find_element_by_xpath(self.enter_request_type_description_xpath).send_keys(request_type_description)

    def select_workflow(self,workflowname):
        select_workflow = Select(self.driver.find_element_by_xpath(self.select_workflow_name_xpath))
        if workflowname == self.getWorkflowName():
            select_workflow.select_by_visible_text(workflowname)
        else:
            print("Workflow is needed to create a request type")

    def select_request_form(self,requestform):
        select_requestform = Select(self.driver.find_element_by_xpath(self.select_form_name_xpath))
        if requestform == self.getFormname():
            select_requestform.select_by_visible_text(requestform)
        else:
            print("Form name required to create the request type")

    def add_request_type(self):
        self.driver.find_element_by_xpath(self.add_request_type_xpath).click()
