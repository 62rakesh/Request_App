from selenium import webdriver
from selenium.webdriver.support.select import Select
from PageObjects.request_group import RequestGroup
from Utilities.readProperties import Readconfig
from Resources.role_locator import role


class assign_group(role, RequestGroup, Readconfig):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver = driver

    def click_authorization(self):
        self.driver.find_element_by_xpath(self.authorization_xpath).click()

    def click_roles(self):
        self.driver.find_element_by_xpath(self.roles_xpath).click()

    def select_role(self, role_name):
        self.driver.find_element_by_xpath(self.search_role_xpath).clear()
        self.driver.find_element_by_xpath(self.search_role_xpath).send_keys(role_name)

    def click_three_dot_menu(self):
        self.driver.find_element_by_xpath(self.three_dot_menu_xpath).click()

    def click_manager_role(self):
        self.driver.find_element_by_xpath(self.assign_manager_role_xpath).click()

    def assign_request_group(self):
        self.driver.find_element_by_xpath(self.assign_request_group_xpath).click()

    def select_request_group(self, request_group):
        group = Select(self.driver.find_element_by_xpath(self.select_request_group_xpath))
        if request_group == self.getRequestgroupname():
            group.select_by_visible_text(request_group)
        else:
            print("No request group selected")

    def add_request_group(self):
        self.driver.find_element_by_xpath(self.add_request_group_xpath).click()
