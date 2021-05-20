from selenium import webdriver
import unittest
from selenium.webdriver.common.action_chains import ActionChains
import HtmlTestRunner
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from Projectdemo.Page.Homepage import Homepage
from Projectdemo.Page.AuthenPage import Authenpage
from Projectdemo.Page.SignUpPage import SignUpPage

class Testdemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:\pythonProject\driver\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_1_productpage(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php") #openwweb
        driver.set_page_load_timeout(10)
        driver.find_element_by_xpath("//*[@id='block_top_menu']/ul/li[1]/a").click()
        pagescroll = driver.find_element_by_xpath("//*[@id='center_column']/ul/li[2]")
        driver.execute_script("arguments[0].scrollIntoView();",pagescroll)

    def test_2_click_product(self):
        driver = self.driver
        a = ActionChains(driver)  ##gọi hàm action
        hover = driver.find_element_by_xpath("//*[@id='center_column']/ul/li[2]")
        a.move_to_element(hover).perform() ##move_to_element dùng để làm hover


    def test_3_quick_view_product(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//*[@id='center_column']/ul/li[2]/div/div[1]/div/a[2]").click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//*[@id='category']/div[3]").click()
        WebDriverWait(driver, 10)
        driver.implicitly_wait(10)

    def test_4_view_product(self):
        driver = self.driver
        a = ActionChains(driver)  ##gọi hàm action
        hover = driver.find_element_by_xpath("//*[@id='center_column']/ul/li[2]")
        a.move_to_element(hover).perform()  ##move_to_element dùng để làm hover
        hover.click()
        driver.find_element_by_xpath("//*[@id='quantity_wanted']").clear()
        driver.find_element_by_xpath("//*[@id='quantity_wanted']").send_keys("4")








    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        print("Complete")

