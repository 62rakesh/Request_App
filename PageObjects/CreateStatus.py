from selenium import webdriver
from Resources.status import status
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class CreateStatus(status):

    def __init__(self, driver):
        self.driver = driver

    def search_workflow_name(self,workflow_name):
        self.driver.find_element_by_xpath(self.search_workflow).send_keys(workflow_name)

    def select_workflow(self):
        self.driver.find_element_by_xpath(self.click_workflow).click()

    def click_add_new_status_btn(self):
        self.driver.find_element_by_xpath(self.create_new_status).click()

    def enter_status(self,status1):
        self.driver.find_element_by_xpath(self.enter_status_name).clear()
        self.driver.find_element_by_xpath(self.enter_status_name).send_keys(status1)

    def add_status(self):
        self.driver.find_element_by_xpath(self.Add_new_status).click()

    def enable_assignee_toggle(self):
        self.driver.find_element_by_xpath(self.notification_assignee).click()

    def enable_originator_toggle(self):
        self.driver.find_element_by_xpath(self.notification_originator).click()

    def select_assign_type(self,assignTo):
        select_assigntype = Select(self.driver.find_element_by_xpath(self.assigntype))
        if assignTo == "Manager":
            self.user = select_assigntype.select_by_visible_text(assignTo)

        elif assignTo == "Originator":
            self.user = select_assigntype.select_by_visible_text(assignTo)

        elif assignTo == "Position":
            self.user = select_assigntype.select_by_value(assignTo)

        else:
            self.user = self.driver.find_element_by_xpath(self.assigntype)
        # JavaScript execution method
        # self.driver.execute_script("arguments[0].click();", self.user)

    def select_fixed_value(self,valuename):
        select_fixed_value = Select(self.driver.find_element_by_xpath(self.fixedvalue))
        if valuename == "Review":
            self.value = select_fixed_value.select_by_visible_text(valuename)

        elif valuename == "Update":
            self.value = select_fixed_value.select_by_visible_text(valuename)

        elif valuename == "End approved":
            self.value = select_fixed_value.select_by_visible_text(valuename)

        elif valuename == "End rejected":
            self.value = select_fixed_value.select_by_visible_text(valuename)

        else:
            self.value = select_fixed_value.select_by_visible_text("Review")







