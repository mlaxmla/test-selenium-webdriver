# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        print(by, value)

    def after_find(self, by, value, driver):
        print(by, value, "found")

    def on_exception(self, exception, driver):
        print(exception)


class TestCaseAdminCategoriesProducts(unittest.TestCase):
    def setUp(self):
        dc = DesiredCapabilities.CHROME
        dc['goog:loggingPrefs'] = {'browser': 'ALL'}  # performance
        self.wd = EventFiringWebDriver(webdriver.Chrome(desired_capabilities=dc, executable_path="D:/Python36/chromedriver.exe"), MyListener())
        self.wd.implicitly_wait(5)

    def test_admin_categories_products(self):
        wd = self.wd
        wait = WebDriverWait(self.wd, 10)
        # 1) wejść w panel administracyjny,
        wd.get("http://localhost/litecart/admin/login.php")
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys("admin")
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("admin")
        wd.find_element_by_name("login").click()
        # 2) otwarcie w katalogu kategorii, która zawiera towary (http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1),
        wd.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
        # 3) konsekwentne otwieranie stron towarów i sprawdzanie, czy nie pojawiają się w logach przeglądarki komunikaty (dowolnego poziomu),
        products_cat1_elements = wd.find_elements(By.XPATH, "//*[@id='content']//a[contains(@href,'http://localhost/litecart/admin/?app=catalog&doc=edit_product&category_id=1')][@title]")
        products_cat1_hrefs_list = []
        for element in products_cat1_elements:
            products_cat1_href = element.get_attribute("href")
            products_cat1_hrefs_list.append(products_cat1_href)
        for product_cat1 in products_cat1_hrefs_list:
            wd.get(product_cat1)
            wait.until(EC.presence_of_element_located((By.NAME, "save")))
            wd.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
        for entry in wd.get_log('browser'):  # performance
            print(entry)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
