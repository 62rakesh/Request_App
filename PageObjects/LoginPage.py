import selenium
from selenium import webdriver
from Resources.loginPage_locator import loginPage_Locator


class Login(loginPage_Locator):

    def __init__(self, driver):
        self.driver = driver

    def set_Username(self,username):
        self.driver.find_element_by_xpath(self.login_uname_xpath).clear()
        self.driver.find_element_by_xpath(self.login_uname_xpath).send_keys(username)

    def click_next_btn(self):
        self.driver.find_element_by_xpath(self.login_next_button_xpath).click()

    def set_password(self,password):
        self.driver.find_element_by_xpath(self.login_upwd_xpath).clear()
        self.driver.find_element_by_xpath(self.login_upwd_xpath).send_keys(password)

    def click_signin_btn(self):
        self.driver.find_element_by_xpath(self.login_signin_xpath).click()

    def click_confirm_btn(self):
        self.driver.find_element_by_xpath(self.login_confirm_xpath).click()

    def capture_text(self):
        self.driver.find_element_by_xpath(self.login_verify_dashboard)

    def click_user_profile(self):
        self.driver.find_element_by_xpath(self.login_profile_xpath).click()

    def logout_user(self):
        self.driver.find_element_by_xpath(self.login_logout_xpath).click()



