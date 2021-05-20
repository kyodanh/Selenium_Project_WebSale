from Projectdemo.Locator.MyAccount import MyAccount

class MyAccountPage():

    def __init__(self, driver):
        self.driver = driver

        self.button_signin = MyAccount.butotn_signin
        self.email = MyAccount.email
        self.password = MyAccount.password
        self.button_login = MyAccount.button_login
        self.button_username = MyAccount.username

    def click_button_signin(self):
        self.driver.find_element_by_xpath(self.button_signin).click()

    def input_email(self, email):
        self.driver.find_element_by_xpath(self.email).clear()
        self.driver.find_element_by_xpath(self.email).send_keys(email)

    def input_password(self, password):
        self.driver.find_element_by_xpath(self.password).clear()
        self.driver.find_element_by_xpath(self.password).send_keys(password)

    def click_button_login(self):
        self.driver.find_element_by_xpath(self.button_login).click()

    def check_username(self, username):
        print(self.driver.find_element_by_xpath(self.button_username).text)
        if self.driver.find_element_by_xpath(self.button_username).text == username:
            print("Correct email")
        else:
            print("False email")

