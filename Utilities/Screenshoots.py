from selenium import webdriver
import io
from PIL import Image
from Testcases.conftest import setup

path = ".\\Screenshoots\\"


class Screenshot:

    def take_screenshot(self):
        self.driver = webdriver.Chrome()
        image = self.driver.get_screenshot_as_file(".\\Screenshoots\\")
        image.save()
        return image

