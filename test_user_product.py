# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestCaseUserProduct(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path="D:/Python36/chromedriver.exe")
        self.wd.implicitly_wait(20)

    def test_user_product(self):
        wd = self.wd
        wd.get("http://localhost/litecart/")
        first_product_element = wd.find_element(By.XPATH, "//*[@id='box-campaigns']/div/ul/li/a[@class='link']")
        first_product_name = wd.find_element(By.XPATH, "//*[@id='box-campaigns']//div[@class='name']").text
        first_product_regularprice = wd.find_element(By.XPATH, "//*[@id='box-campaigns']//a[1]//s[@class='regular-price']")
        first_product_regularprice_color = first_product_regularprice.value_of_css_property("color")
        assert first_product_regularprice_color == 'rgba(119, 119, 119, 1)'
        first_product_regularprice_strikethrough = first_product_regularprice.value_of_css_property("text-decoration")
        assert first_product_regularprice_strikethrough == 'line-through solid rgb(119, 119, 119)'
        first_product_regularprice_value = first_product_regularprice.text
        first_product_campaignprice = wd.find_element(By.XPATH, "//*[@id='box-campaigns']//a[1]//strong[@class='campaign-price']")
        first_product_campaignprice_color = first_product_campaignprice.value_of_css_property("color")
        assert first_product_campaignprice_color == 'rgba(204, 0, 0, 1)'
        first_product_campaignprice_fontweight = first_product_campaignprice.value_of_css_property("font-weight")
        assert first_product_campaignprice_fontweight == '700'
        first_product_campaignprice_value = first_product_campaignprice.text
        first_product_element.click()
        product_title = wd.find_element(By.XPATH, "//*[@id='box-product']//h1[@class='title']").text
        assert first_product_name == product_title
        product_regularprice = wd.find_element(By.XPATH, "//*[@id='box-product']//s[@class='regular-price']")
        product_regularprice_color = product_regularprice.value_of_css_property("color")
        assert product_regularprice_color == 'rgba(102, 102, 102, 1)'
        product_regularprice_strikethrough = product_regularprice.value_of_css_property("text-decoration")
        assert product_regularprice_strikethrough == 'line-through solid rgb(102, 102, 102)'
        product_regularprice_value = product_regularprice.text
        product_campaignprice = wd.find_element(By.XPATH, "//*[@id='box-product']//strong[@class='campaign-price']")
        product_campaignprice_color = product_campaignprice.value_of_css_property("color")
        assert product_campaignprice_color == 'rgba(204, 0, 0, 1)'
        product_campaignprice_fontweight = product_campaignprice.value_of_css_property("font-weight")
        assert product_campaignprice_fontweight == '700'
        assert first_product_regularprice_value == product_regularprice_value
        product_campaignprice_value = product_campaignprice.text
        assert first_product_campaignprice_value == product_campaignprice_value

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
