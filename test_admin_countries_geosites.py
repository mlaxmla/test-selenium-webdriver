# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestCaseAdminCountriesGeosites(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path="D:/Python36/chromedriver.exe")
        self.wd.implicitly_wait(20)

    def test_admin_countries(self):
        wd = self.wd
        wd.get("http://localhost/litecart/admin/login.php")
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys("admin")
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("admin")
        wd.find_element_by_name("login").click()
        wd.get("http://localhost/litecart/admin/?app=countries&doc=countries")
        countries_lists = wd.find_elements(By.XPATH, "//*[@id='content']/form/table/tbody//td[5]/a")
        country_names_list = []
        for country in countries_lists:
            country_name = country.text
            country_names_list.append(country_name)
        assert sorted(country_names_list) == country_names_list
        countries_with_zones_lists = wd.find_elements(By.XPATH, "//*[@id='content']/form/table/tbody//td[6][.!='0']/../td/a[(@title)]")
        for country_with_zone in countries_with_zones_lists:
            country_with_zone_href = country_with_zone.get_attribute("href")
            wd.get(country_with_zone_href)
            zones_lists = wd.find_elements(By.XPATH, "//*[@id='table-zones']/tbody//td[3]/input[@type='hidden']/..")
            zone_names_list = []
            for zone in zones_lists:
                zone_name = zone.text
                zone_names_list.append(zone_name)
                return zone_names_list
            assert sorted(zone_names_list) == zone_names_list
            wd.get("http://localhost/litecart/admin/?app=countries&doc=countries")

    def test_admin_geozones(self):
        wd = self.wd
        wd.get("http://localhost/litecart/admin/login.php")
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys("admin")
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("admin")
        wd.find_element_by_name("login").click()
        wd.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
        countriesgeo_lists = wd.find_elements(By.XPATH, "//*[@id='content']/form/table/tbody//td[3]/a")
        for countrygeo in countriesgeo_lists:
            countrygeo_href = countrygeo.get_attribute("href")
            wd.get(countrygeo_href)
            geozones_lists = wd.find_elements(By.XPATH, "//*[@id='table-zones']/tbody//td[3]/select/option[@selected='selected']")
            geozone_names_list = []
            for geozone in geozones_lists:
                geozone_name = geozone.text
                geozone_names_list.append(geozone_name)
                return geozone_names_list
            assert sorted(geozone_names_list) == geozone_names_list
            wd.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
            return

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
