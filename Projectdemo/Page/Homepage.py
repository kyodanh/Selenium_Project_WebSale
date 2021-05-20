from Projectdemo.Locator.Home import Home
class Homepage():

    def __init__(self, driver):

        self.driver = driver

        self.button_signin = Home.button_signin

    def click_button_signin(self):
        self.driver.find_element_by_xpath(self.button_signin).click()

