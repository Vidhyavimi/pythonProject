from selenium import webdriver
import time
import unittest
import sys
import pytest
sys.path.append("C:\\Users\Vidhya\PycharmProjects\pythonProject")
from Projects.ATProject2.TCPIM03.Pages.homepage import login_page
from Projects.ATProject2.TCPIM03.Pages.adminsidepanel_page import adminsidepanel_page




class admin_header_validation_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_admin_header(self):

        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")

        Login = login_page(driver)
        Login.enter_username("Admin")
        Login.enter_password("admin123")
        Login.click_login()

        Admin = adminsidepanel_page(driver)
        Admin.sidepanel_validation()
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):  # overriding tearDownClass
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
