# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestCaseAdminMenuItems(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path="D:/Python36/chromedriver.exe")
        self.wd.implicitly_wait(20)

    def test_admin_menuitems(self):
        wd = self.wd
        wd.get("http://localhost/litecart/admin/login.php")
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys("admin")
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("admin")
        wd.find_element_by_name("login").click()
        # links_list = wd.find_elements(By.XPATH, "//li[@id='app-']/a/span[@class='name']/..")
        elements_list = wd.find_elements(By.XPATH, "//li[@id='app-']/a/span[@class='name']")
        ahrefs_list = wd.find_elements(By.XPATH, "//li[@id='app-']/a/span[@class='name']/..")
        names_list = []
        hrefs_list = []
        headers_list = []
        headers_expected_list = ['Template', 'Catalog', 'Countries', 'Currencies', 'Customers', 'Geo Zones', 'Languages', 'Job Modules', 'Orders', 'Pages', ' Monthly Sales', 'Settings', 'Slides', 'Tax Classes', ' Search Translations', 'Users', 'vQmods']
        for nameitem, hrefitem, headerexpecteditem in zip(elements_list, ahrefs_list, headers_expected_list):
            name = nameitem.text
            names_list.append(name)
            href = hrefitem.get_attribute("href")
            hrefs_list.append(href)
            # i don't know how to iterate over these lists in python and go to correct address :(
#            wd.get(href)
#            wd.find_element_by_xpath(hrefitem).click()
#            header = wd.find_element_by_tag_name('H1')
#            headers_list.append(header)
#            assert header.text == headerexpecteditem
#            wd.get("http://localhost/litecart/admin/")
        return names_list, hrefs_list, headers_list

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
