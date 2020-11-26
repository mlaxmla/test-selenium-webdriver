# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random, string, time
import unittest

new_user_random_email = (''.join(random.choice(string.ascii_lowercase) for i in range(8))) + "@guuuuugl.pl"

class TestCaseUserCreateAccount(unittest.TestCase):

    def setUp(self):
        self.wd = webdriver.Chrome(executable_path="D:/Python36/chromedriver.exe")
        self.wd.implicitly_wait(20)

    def test1_user_create_account(self):
        global new_user_random_email
        # 1)    Rejestracja nowego konta z unikalnym adresem mailowym (tak, aby nie kolidował z wcześniej utworzonymi użytkownikami),
        wd = self.wd
        wd.get("http://localhost/litecart/en/create_account")
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("firstname_testdata")
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("firstname_testdata")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("lastname_testdata")
        wd.find_element_by_name("address1").clear()
        wd.find_element_by_name("address1").send_keys("address1_testdata")
        wd.find_element_by_name("postcode").clear()
        wd.find_element_by_name("postcode").send_keys("6798")
        wd.find_element_by_name("city").clear()
        wd.find_element_by_name("city").send_keys("city_testdata")
        Select(wd.find_element(By.XPATH, "//*[@name='country_code']")).select_by_visible_text("Christmas Island")
        wd.find_element_by_name("phone").clear()
        wd.find_element_by_name("phone").send_keys("+6112345678")
        wd.find_element_by_name("email").clear()
        # new_user_random_email = (''.join(random.choice(string.ascii_lowercase) for i in range(8)))+"@guuuuugl.pl"
        wd.find_element_by_name("email").send_keys(new_user_random_email)
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("password")
        wd.find_element_by_name("confirmed_password").clear()
        wd.find_element_by_name("confirmed_password").send_keys("password")
        wd.find_element_by_name("create_account").click()
        WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='notices']/div[contains(text(),'Your customer account has been created.')]")))
        # 2)    Wylogowanie (logout), ponieważ po udanej rejestracji następuje automatyczne zalogowanie
        WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='box-account']//a[@href='http://localhost/litecart/en/logout']")))
        ## time.sleep(2)
        ### why the following click() doesn't work during test execution without above time.sleep()? (it works when manually executed in a python console; please provide me some explenation and better solution, which will eliminate sleep())
        wd.find_element_by_xpath("//*[@id='box-account']//a[@href='http://localhost/litecart/en/logout']").click()
        ### with sleep() before click(), presence and visibility seems to work, but which condition check is better in this situation and why?
        # WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='notices']/div[contains(text(),'You are now logged out.')]")))
        WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='notices']/div[contains(text(),'You are now logged out.')]")))

    def test2_new_user_login(self):
        global new_user_random_email
        # 3)    Ponowne zalogowanie na dopiero co utworzone konto
        wd = self.wd
        wd.get("http://localhost/litecart/en/")
        wd.find_element_by_name("email").send_keys(new_user_random_email)
        wd.find_element_by_name("password").send_keys("password")
        wd.find_element_by_name("login").click()
        WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='notices']/div[contains(text(),'You are now logged in as')]")))
        # 4)    Ponowne wylogowanie
        ### please provide me with example how to organize test project to enable an effective use of methods, variables etc.
        ### here the problematic solution from previous test works as exected without sleep() - I don't understand why...
        wd.find_element_by_xpath("//*[@id='box-account']//a[@href='http://localhost/litecart/en/logout']").click()
        WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='notices']/div[contains(text(),'You are now logged out.')]")))

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
            unittest.main()





