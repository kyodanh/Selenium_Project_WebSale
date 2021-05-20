from Projectdemo.Locator.SignUp import SignUp
from selenium.webdriver.support.ui import Select

class SignUpPage():

    def __init__(self, driver):

        self.driver = driver

        self.button_title = SignUp.radio_button_title
        self.first_name = SignUp.frist_name
        self.last_name = SignUp.last_name
        self.email = SignUp.email
        self.value = SignUp.value
        self.password = SignUp.password
        self.day = SignUp.select_day
        self.month = SignUp.select_month
        self.year = SignUp.select_year
        self.cus_fname = SignUp.cus_fname
        self.cus_lname = SignUp.cus_lname
        self.compamy = SignUp.company
        self.address_1 = SignUp.address_1
        self.address_2 = SignUp.address_2
        self.city = SignUp.city
        self.stage = SignUp.state
        self.postcode = SignUp.post_code
        self.country = SignUp.country
        self.other = SignUp.other
        self.phone_1 = SignUp.phone_1
        self.phone_2 = SignUp.phone_2
        self.alias = SignUp.alias
        self.button_summit = SignUp.button_submit


    def click_radio_button(self):
        self.driver.find_element_by_xpath(self.button_title).click()

    def input_fname(self, fname):
        self.driver.find_element_by_xpath(self.first_name).clear()
        self.driver.find_element_by_xpath(self.first_name).send_keys(fname)

    def input_lname(self, lname):
        self.driver.find_element_by_xpath(self.last_name).clear()
        self.driver.find_element_by_xpath(self.last_name).send_keys(lname)

    def check_email(self, email):
        print(self.driver.find_element_by_name(self.email).get_attribute(self.value))
        if self.driver.find_element_by_name(self.email).get_attribute(self.value) == email:
            print("Correct email")
        else:
            print("False email")

    def input_password(self, passw):
        self.driver.find_element_by_xpath(self.password).clear()
        self.driver.find_element_by_xpath(self.password).send_keys(passw)

    def select_day(self,value_day):
        select = Select(self.driver.find_element_by_xpath(self.day))
        select.select_by_value(value_day)

    def select_month(self,value_month):
        select = Select(self.driver.find_element_by_xpath(self.month))
        select.select_by_value(value_month)

    def select_year(self,value_year):
        select = Select(self.driver.find_element_by_xpath(self.year))
        select.select_by_value(value_year)

    def input_cusfname(self, cus_fname):
        self.driver.find_element_by_xpath(self.cus_fname).clear()
        self.driver.find_element_by_xpath(self.cus_fname).send_keys(cus_fname)

    def input_cuslname(self, cus_lname):
        self.driver.find_element_by_xpath(self.cus_lname).clear()
        self.driver.find_element_by_xpath(self.cus_lname).send_keys(cus_lname)

    def input_company(self, company):
        self.driver.find_element_by_xpath(self.compamy).clear()
        self.driver.find_element_by_xpath(self.compamy).send_keys(company)

    def input_add1(self, add1):
        self.driver.find_element_by_xpath(self.address_1).clear()
        self.driver.find_element_by_xpath(self.address_1).send_keys(add1)

    def input_add2(self, add2):
        self.driver.find_element_by_xpath(self.address_2).clear()
        self.driver.find_element_by_xpath(self.address_2).send_keys(add2)

    def input_city(self, city):
        self.driver.find_element_by_xpath(self.city).clear()
        self.driver.find_element_by_xpath(self.city).send_keys(city)

    def select_stage(self, stage):
        select = Select(self.driver.find_element_by_xpath(self.stage))
        select.select_by_value(stage)

    def input_postcode(self, post):
        self.driver.find_element_by_xpath(self.postcode).clear()
        self.driver.find_element_by_xpath(self.postcode).send_keys(post)

    def select_country(self, count):
        select = Select(self.driver.find_element_by_xpath(self.country))
        select.select_by_value(count)

    def input_other(self, other):
        self.driver.find_element_by_xpath(self.other).clear()
        self.driver.find_element_by_xpath(self.other).send_keys(other)

    def input_phone_1(self, phone_1):
        self.driver.find_element_by_xpath(self.phone_1).clear()
        self.driver.find_element_by_xpath(self.phone_1).send_keys(phone_1)

    def input_phone_1(self, phone_1):
        self.driver.find_element_by_xpath(self.phone_1).clear()
        self.driver.find_element_by_xpath(self.phone_1).send_keys(phone_1)

    def input_phone_2(self, phone_2):
        self.driver.find_element_by_xpath(self.phone_2).clear()
        self.driver.find_element_by_xpath(self.phone_2).send_keys(phone_2)

    def input_assign(self, assign):
        self.driver.find_element_by_xpath(self.alias).clear()
        self.driver.find_element_by_xpath(self.alias).send_keys(assign)

    def click_button_summit(self):
        self.driver.find_element_by_xpath(self.button_summit).click()