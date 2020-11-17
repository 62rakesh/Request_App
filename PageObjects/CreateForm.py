from selenium import webdriver
from selenium.webdriver.support.select import Select
from Resources.hireform_locator import hire_locator


class CreateForm(hire_locator):

    def __init__(self, driver):
        self.driver = driver

    def click_drop_down_menu(self):
        self.driver.find_element_by_xpath(self.dropdown_xpath).click()

    def select_admin_from_the_drop_down_menu(self):
        self.driver.find_element_by_xpath(self.admin_menu_xpath).click()

    def click_breadcrumb_menu(self):
        self.driver.find_element_by_xpath(self.breadcrumb_xpath).click()

    def click_form_management_menu(self):
        self.driver.find_element_by_xpath(self.form_management_menu_xpath).click()

    def click_forms_button(self):
        self.driver.find_element_by_xpath(self.form_child_xpath).click()

    def click_add_form_button(self):
        self.driver.find_element_by_xpath(self.new_btn_xpath).click()

    def enable_form_template_toggle(self):
        self.driver.find_element_by_xpath(self.form_template_toggle_xpath).click()

    def select_template_name(self,template):
        form_template = Select(self.driver.find_element_by_xpath(self.template_dropdown_xpath))
        if template == "New hire":
            self.template_name = form_template.select_by_visible_text(template)

        elif template == "New position":
            self.template_name = form_template.select_by_visible_text(template)

        elif template == "Change of terms":
            self.template_name = form_template.select_by_visible_text(template)

        elif template == "Request overlapping position":
            self.template_name = form_template.select_by_visible_text(template)

        elif template == "Request to release employee":
            self.template_name = form_template.select_by_visible_text(template)

        elif template == "Termination":
            self.template_name = form_template.select_by_visible_text(template)

        else:
            form_template.select_by_visible_text("New hire")

    def enter_form_name(self,formname):
        self.driver.find_element_by_xpath(self.enter_name_xpath).clear()
        self.driver.find_element_by_xpath(self.enter_name_xpath).send_keys(formname)

    def enter_descripton(self,formdescription):
        self.driver.find_element_by_xpath(self.description_xpath).clear()
        self.driver.find_element_by_xpath(self.description_xpath).send_keys(formdescription)

    def select_message_type(self,message_type):
        form_message_type = Select(self.driver.find_element_by_xpath(self.message_type_xpath))
        if message_type == "Hire":
            self.message_type_name = form_message_type.select_by_visible_text(message_type)

        elif message_type == "New Position":
            self.message_type_name = form_message_type.select_by_visible_text(message_type)

        elif message_type == "Terminations":
            self.message_type_name = form_message_type.select_by_visible_text(message_type)

        elif message_type == " ":
            self.message_type_name = form_message_type.select_by_visible_text(message_type)

        else:
            form_message_type.select_by_visible_text(" ")

    def add_request_form(self):
        self.driver.find_element_by_xpath(self.add_btn_xpath).click()

