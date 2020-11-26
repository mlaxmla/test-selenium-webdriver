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
        countries_with_zones_elements = wd.find_elements(By.XPATH, "//*[@id='content']/form/table/tbody//td[6][.!='0']/../td/a[(@title)]")
        countries_with_zones_hrefs_list = []
        for element in countries_with_zones_elements:
            country_with_zone_href = element.get_attribute("href")
            countries_with_zones_hrefs_list.append(country_with_zone_href)
        for country_with_zone in countries_with_zones_hrefs_list:
            wd.get(country_with_zone)
            zones_lists = wd.find_elements(By.XPATH, "//*[@id='table-zones']/tbody//td[3]/input[@type='hidden']/..")
            zone_names_list = []
            for zone in zones_lists:
                zone_name = zone.text
                zone_names_list.append(zone_name)
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
        countriesgeo_elements = wd.find_elements(By.XPATH, "//*[@id='content']/form/table/tbody//td[3]/a")
        countriesgeo_hrefs_list = []
        for element in countriesgeo_elements:
            countrygeo_href = element.get_attribute("href")
            countriesgeo_hrefs_list.append(countrygeo_href)
        for countrygeo in countriesgeo_hrefs_list:
            wd.get(countrygeo)
            geozones_lists = wd.find_elements(By.XPATH, "//*[@id='table-zones']/tbody//td[3]/select/option[@selected='selected']")
            geozone_names_list = []
            for geozone in geozones_lists:
                geozone_name = geozone.text
                geozone_names_list.append(geozone_name)
            assert sorted(geozone_names_list) == geozone_names_list
            wd.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
