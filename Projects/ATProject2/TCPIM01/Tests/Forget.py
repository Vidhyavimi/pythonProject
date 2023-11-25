from selenium import webdriver
import time
import unittest
import pytest
import sys
sys.path.append("C:\\Users\Vidhya\PycharmProjects\pythonProject")
from Projects.ATProject2.TCPIM01.Pages.fp_page import Fp_Page
from Projects.ATProject2.TCPIM01.Pages.rp_page import rp_page




class Forget_Password_Test (unittest.TestCase):

    @classmethod
    def setUpClass(cls):  #intializing the web driver
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_Forget_Password_Valid(self):   #test function starts
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        Fpage = Fp_Page(driver)   #instantiate the Fp_Page class
        time.sleep(2)
        Fpage.click_forget()
        time.sleep(2)

        Rpage = rp_page(driver)    #instantiate the rp_page class
        Rpage.enter_username("Admin")
        time.sleep(2)
        Rpage.click_reset()
        time.sleep(2)


    @classmethod
    def tearDownClass(cls):     #overriding tearDownClass
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")






