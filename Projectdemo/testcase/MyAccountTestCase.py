from selenium import webdriver
import unittest
import HtmlTestRunner
from selenium.webdriver.support.ui import Select

from Projectdemo.Page.Homepage import Homepage
from Projectdemo.Page.MyAccountPage import MyAccountPage

class Testdemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:\pythonProject\driver\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_1_home_page(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php") #openwweb
        driver.set_page_load_timeout(10)
        homepage = Homepage(driver) #đặt biến homepage từ class homepage đê gọi
        homepage.click_button_signin()
        driver.set_page_load_timeout(10)
        navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
        responseStart = driver.execute_script("return window.performance.timing.responseStart")
        domComplete = driver.execute_script("return window.performance.timing.domComplete")
        backendPerformance_calc = responseStart - navigationStart
        frontendPerformance_calc = domComplete - responseStart
        print("Back End: %s" % backendPerformance_calc)
        print("Front End: %s" % frontendPerformance_calc)


    def test_2_open_signin_page(self):
        driver = self.driver
        signin = MyAccountPage(driver)
        signin.click_button_signin()


    def test_3_login(self):
        driver = self.driver
        login = MyAccountPage(driver)
        login.input_email("kyodanh@gmail.com")
        login.input_password("dannguyen0803")
        login.click_button_login()

    def test_4_myAccount(self):
        driver = self.driver
        myaccount = MyAccountPage(driver)
        myaccount.check_username("Dan test")



    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        print("Complete")

