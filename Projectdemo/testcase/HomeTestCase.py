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
        driver.find_element_by_xpath("//*[@id='block_top_menu']/ul/li[1]/a").click()
        # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") ##scrolldown xuống cuối trang
        # driver.set_page_load_timeout(10)
        # women = driver.find_element_by_xpath("//*[@id='block_top_menu']/ul/li[1]/a")
        # driver.execute_script("arguments[0].scrollIntoView();",women)






    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        print("Complete")

