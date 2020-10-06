from selenium import webdriver
from Resources.Workflow_locator import workflow_locator


class CreateWorkflow(workflow_locator):

    def __init__(self, driver):
        self.driver = driver

    def click_drop_down_menu(self):
        self.driver.find_element_by_xpath(self.dropdown_xpath).click()

    def select_admin_from_the_drop_down_menu(self):
        self.driver.find_element_by_xpath(self.admin_menu_xpath).click()

    def click_breadcrumb_menu(self):
        self.driver.find_element_by_xpath(self.breadcrumb_xpath).click()

    def click_workflow_menu(self):
        self.driver.find_element_by_xpath(self.workflow_menu_xpath).click()

    def click_workflow_sub_menu(self):
        self.driver.find_element_by_xpath(self.workflow_submenu_xpath).click()

    def click_new_button(self):
        self.driver.find_element_by_xpath(self.new_btn_xpath).click()

    def enter_workflow_name(self,workflowname):
        self.driver.find_element_by_xpath(self.workflow_name_xpath).clear()
        self.driver.find_element_by_xpath(self.workflow_name_xpath).send_keys(workflowname)

    def enter_workflow_description(self, description):
        self.driver.find_element_by_xpath(self.workflow_description_xpath).clear()
        self.driver.find_element_by_xpath(self.workflow_description_xpath).send_keys(description)

    def active_toggle(self):
        self.driver.find_element_by_xpath(self.active_toggle_xpath).click()

    def add_workflow(self):
        self.driver.find_element_by_xpath(self.add_button_xpath).click()

