import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.LoginPage import Login
from Utilities.CustomLogger import LogGen
from Utilities.readProperties import Readconfig
from Utilities.Screenshoots import Screenshot


class Test_001_Login:
    base_url = Readconfig.getApplicationURL()
    username = Readconfig.getUsername()
    Password = Readconfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_home(self, setup):
        self.logger.info("############ Executing testcase TC_001_login ########### ")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        title = self.driver.title
        print(title)
        print("Login page successfully launched")
        self.driver.close()
        self.logger.info("############ The browser is launched successfully ########### ")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("############ Setting up with the login test execution ########### ")
        self.driver=setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.lp=Login(self.driver)
        self.lp.set_Username(self.username)
        time.sleep(1)
        self.lp.click_next_btn()
        time.sleep(1)
        self.lp.set_password(self.Password)
        time.sleep(1)
        self.lp.click_signin_btn()
        time.sleep(1)
        self.lp.click_confirm_btn()
        time.sleep(3)
        self.driver.get_screenshot_as_file(".\\Screenshoots\\login.png")
        self.logger.info("############ User is successfully logged in ########### ")
        print("Login is successfully completed")
        self.driver.close()

    @pytest.mark.sanity
    def test_logout(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.set_Username(self.username)
        time.sleep(1)
        self.lp.click_next_btn()
        time.sleep(1)
        self.lp.set_password(self.Password)
        time.sleep(1)
        self.lp.click_signin_btn()
        time.sleep(1)
        self.lp.click_confirm_btn()
        time.sleep(1)
        print("Login is successfully completed")
        dashboard_text = self.lp.capture_text()
        print(dashboard_text)
        title = self.driver.title
        print(title)
        self.lp.click_user_profile()
        time.sleep(1)
        self.lp.logout_user()
        time.sleep(3)
        self.logger.info("############ User is successfully logged out ########### ")
        print("User is logged out")
        self.driver.close()












