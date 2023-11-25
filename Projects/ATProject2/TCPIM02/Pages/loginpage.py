from selenium.webdriver.common.by import By

class login_page():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox = "username"
        self.username = "Admin"
        self.password_textbox = "password"
        self.password = "admin123"
        self.login_button = "//button"

    def enter_username(self, username):    #method for entering username
        self.driver.find_element("name",self.username_textbox).send_keys(self.username)

    def enter_password(self, password):    #method for entering password
        self.driver.find_element("name",self.password_textbox).send_keys(self.password)

    def click_login(self):        #method for clicking login button
        self.driver.find_element(By.XPATH,self.login_button).click()