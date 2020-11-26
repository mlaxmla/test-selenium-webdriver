# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time


class TestCaseAdminNewProduct(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path="D:/Python36/chromedriver.exe")
        self.wd.implicitly_wait(20)

    def test_admin_new_product(self):
        wd = self.wd
        wd.get("http://localhost/litecart/admin/login.php")
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys("admin")
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("admin")
        wd.find_element_by_name("login").click()
        # Stwórz scenariusz dodania nowego artykułu (produktu) w aplikacji litecart (przez panel administracyjny).
        # Aby dodać przedmiot należy otworzyć menu Catalog, kliknąć w przycisk Add New Product znajdujący w prawym górnym rogu, wypełnić pola z informacją o artykule i zapisać.
        # Wystarczy wypełnić tylko informacje na kartach General, Information i Prices. Na tej ostatniej nie ma potrzeby dodawania rabatu (Compains).
        # todo: what is the better way to wait the next steps of test in this case?
        time.sleep(2)
        wd.find_element(By.XPATH, "//li[@id='app-']/a/span[@class='name'][.='Catalog']").click()
        nametestdata_len = len(wd.find_elements(By.XPATH, "//*[@id='content']//table[@class='dataTable']//a[.='name[en]_testdata']"))
        # todo: what is the better way to wait the next steps of test in this case?
        time.sleep(2)
        # WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='box-account']//a[@href='http://localhost/litecart/en/logout']")))
        # WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Add New Product")))
        wd.find_element_by_link_text("Add New Product").click()
        # todo: what is the better way to wait the next steps of test in this case?
        time.sleep(2)
        wd.find_element_by_name("name[en]").send_keys("name[en]_testdata")
        wd.find_element(By.XPATH, "//*[@id='content']//a[.='Information']").click()
        Select(wd.find_element_by_name("manufacturer_id")).select_by_visible_text("ACME Corp.")
        wd.find_element(By.XPATH, "//*[@id='content']//a[.='Prices']").click()
        wd.find_element_by_name("purchase_price").clear()
        wd.find_element_by_name("purchase_price").send_keys("1,00")
        Select(wd.find_element_by_name("purchase_price_currency_code")).select_by_visible_text("US Dollars")
        wd.find_element_by_name("save").click()
        # Po zapisaniu artykułu w panelu administracyjnym należy upewnić się, że pojawił się w katalogu.
        # W części sklepu, przeznaczonej dla klientów nie trzeba tego sprawdzać.
        assert nametestdata_len+1 == len(wd.find_elements(By.XPATH, "//*[@id='content']//table[@class='dataTable']//a[.='name[en]_testdata']"))

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
