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
        # 1)    Wejście do panelu administratora http://localhost/litecart/admin.
        wd.get("http://localhost/litecart/admin/login.php")
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys("admin")
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("admin")
        wd.find_element_by_name("login").click()
        # 2)    Klikanie kolejno na wszystkie punkty w menu z lewej strony, w tym w zagnieżdżone punkty.
        ahrefs_list = wd.find_elements(By.XPATH, "//li[@id='app-']//a")
        names_list = []
        hrefs_list = []
        for element in ahrefs_list:
            name = element.find_element_by_class_name("name").text
            names_list.append(name)
            href = element.get_attribute("href")
            hrefs_list.append(href)
        # 3)    Dla każdej strony sprawdzenie nagłówka (to znaczy elementu z tagiem h1).
        headers_expected_list = ['Template', 'Catalog', 'Countries', 'Currencies', 'Customers', 'Geo Zones', 'Languages', 'Job Modules', 'Orders', 'Pages', 'Monthly Sales', 'Settings', 'Slides', 'Tax Classes', 'Search Translations', 'Users', 'vQmods']
        for nameitem, hrefitem, headerexpecteditem in zip(names_list, hrefs_list, headers_expected_list):
            wd.get(hrefitem)
            header = wd.find_element_by_tag_name('H1').text
            assert header == headerexpecteditem
            wd.get("http://localhost/litecart/admin/")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
