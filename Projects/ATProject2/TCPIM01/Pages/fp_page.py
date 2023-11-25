from selenium.webdriver.common.by import By
class Fp_Page():

    def __init__(self, driver):  #class initialization
        self.driver = driver

        self.forget_text =  "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']"


    def click_forget(self):      #method for clicking forget password

         self.driver.find_element(By.XPATH,self.forget_text).click()





