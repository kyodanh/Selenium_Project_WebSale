from Projectdemo.Locator.Authen import Authen
class Authenpage():

    def __init__(self, driver):
        self.driver = driver

        self.user_name = Authen.user_name

        self.button_create_account = Authen.button_create_account

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.user_name).clear()
        self.driver.find_element_by_xpath(self.user_name).send_keys(username)

    def click_button_signin(self):
        self.driver.find_element_by_xpath(self.button_create_account).click()






# driver.find_element_by_xpath("//*[@id='uniform-id_gender1']/span").click()
# driver.find_element_by_xpath("//*[@id='customer_firstname']").send_keys("Dan")
# driver.find_element_by_xpath("//*[@id='customer_lastname']").send_keys("Nguyen")
# print(driver.find_element_by_name("email").get_attribute('value'))
# if driver.find_element_by_name('email').get_attribute('value') == "kyo": print("Correct email")
# else: print("False email")