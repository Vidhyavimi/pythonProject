from selenium.webdriver.common.by import By

class admin_page():

    def __init__(self,driver):
        self.driver = driver
        self.title = "OrangeHRM"
        self.header = "//span[@class='oxd-topbar-body-nav-tab-item']|//a[@class='oxd-topbar-body-nav-tab-item']"

    def title_validation(self):   #title validation
        element = self.driver.title
        if element =="OrangeHRM":
            pass
        else:
            exit(1)


    def header_validation(self):   #admin header title validation
        l1=['User Management','Job','Organization','Nationalities','Corporate Branding','Configuration','Qualifications']
        l2 =[]
        for elem in self.driver.find_elements(By.XPATH, self.header):
            l2.append(elem.text)

        l1.sort()
        l2.sort()
        if l1 == l2:
            pass
        else:
            exit(1)










