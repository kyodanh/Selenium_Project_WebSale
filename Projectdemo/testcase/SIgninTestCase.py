from selenium import webdriver
import unittest
import HtmlTestRunner
from selenium.webdriver.support.ui import Select

from Projectdemo.Page.Homepage import Homepage
from Projectdemo.Page.AuthenPage import Authenpage
from Projectdemo.Page.SignUpPage import SignUpPage

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


    def test_2_Authen_page(self):
        driver = self.driver
        authen = Authenpage(driver)
        driver.set_page_load_timeout(10)
        authen.enter_username("DanhNC15@gmail.com")
        driver.implicitly_wait(10)
        authen.click_button_signin()

    def test_3_signup_page(self):
        driver = self.driver
        signup = SignUpPage(driver)
        driver.set_page_load_timeout(10)
        signup.click_radio_button()
        signup.input_fname("Dan")
        signup.input_lname("Nguyen")
        signup.check_email("DanhNC15@gmail.com")
        signup.input_password("dannguyen0803")
        signup.select_day("8")
        signup.select_month("3")
        signup.select_year("1998")
        signup.input_cusfname("test")
        signup.input_lname("test")
        signup.input_company("test")
        signup.input_add1("test")
        signup.input_add2("test")
        signup.input_city("test")
        signup.select_stage("5")
        signup.input_postcode("test")
        signup.select_country("21")
        signup.input_other("other")
        signup.input_phone_1("0942058905")
        signup.input_phone_2("0942058905")
        signup.input_assign("test")
        signup.click_button_summit()



    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        print("Complete")

