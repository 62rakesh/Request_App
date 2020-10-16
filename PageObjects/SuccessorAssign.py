from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from Resources.successor import successor


class SuccessorAssign(successor):

    def __init__(self, driver):
        self.driver = driver

    def click_three_dot_icon_manager(self):
        self.driver.find_element_by_xpath(self.three_dot_icon_manager).click()
        # action = ActionChains(self.driver)
        # action.click(on_element=self.three_dot_icon_manager)
        # action.perform()

    def click_three_dot_icon_originator(self):
        self.driver.find_element_by_xpath(self.three_dot_icon_originator).click()
        # action = ActionChains(self.driver)
        # action.click(on_element=self.three_dot_icon_manager)
        # action.perform()

    def click_manager_successor_btn_three_dot_menu(self):
        self.driver.find_element_by_xpath(self.manager_successor_btn).click()

    def click_originator_successor_btn_three_dot_menu(self):
        self.driver.find_element_by_xpath(self.originator_successor_btn).click()

    def click_create_new_successor_btn(self):
        self.driver.find_element_by_xpath(self.create_successor_btn).click()

    def click_add_successor_btn(self):
        self.driver.find_element_by_xpath(self.add_new_successor_btn).click()

    def assign_successor_to_status(self,successor_name):
        assign_successor = Select(self.driver.find_element_by_xpath(self.select_successor_dropdown))
        if successor_name == "Back to originator":
            self.successor_value = assign_successor.select_by_visible_text(successor_name)

        elif successor_name == "Approve":
            self.successor_value = assign_successor.select_by_visible_text(successor_name)

        elif successor_name == "Reject":
            self.successor_value = assign_successor.select_by_visible_text(successor_name)

        elif successor_name == "Back to manager":
            self.successor_value = assign_successor.select_by_visible_text(successor_name)

        else:
            assign_successor.select_by_visible_text("Back to originator")

    def assign_next_status_to_successor(self,nextstatus):
        successor_status = Select(self.driver.find_element_by_xpath(self.select_next_status_dropdown))
        if nextstatus == "Review by originator":
            self.status_value = successor_status.select_by_visible_text(nextstatus)

        elif nextstatus == "Approve":
            self.status_value = successor_status.select_by_visible_text(nextstatus)

        elif nextstatus == "Reject":
            self.status_value = successor_status.select_by_visible_text(nextstatus)

        elif nextstatus == "Review by manager":
            self.status_value = successor_status.select_by_visible_text(nextstatus)

        else:
            successor_status.select_by_visible_text("Review by originator")

    def click_back_button(self):
        self.driver.find_element_by_xpath(self.back_btn).click()





