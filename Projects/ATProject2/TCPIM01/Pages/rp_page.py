from selenium.webdriver.common.by import By

class rp_page():

    def __init__(self, driver):  #class initialization
        self.driver = driver

        self.username_textbox = "username"
        self.username = "admin"
        self.resetpassword_button = "//button[@type='submit']"

    def enter_username(self, username):    #method for entering username
        self.driver.find_element("name",self.username_textbox).send_keys(self.username)

    def click_reset(self):        #method for clicking reset button
        self.driver.find_element(By.XPATH,self.resetpassword_button).click()
