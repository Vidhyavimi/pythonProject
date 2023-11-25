from selenium.webdriver.common.by import By

class adminsidepanel_page():

    def __init__(self,driver):
        self.driver = driver
        self.sidepanel = "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']"


    def sidepanel_validation(self):
        l1=['Admin','PIM','Leave','Time','Recruitment','My Info','Performance','Dashboard','Directory','Maintenance','Claim','Buzz']
        l2 =[]
        for elem in self.driver.find_elements(By.XPATH, self.sidepanel):
            l2.append(elem.text)

        l1.sort()
        l2.sort()
        if l1 == l2:
            pass
        else:
            exit(1)