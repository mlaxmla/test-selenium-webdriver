# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.color import Color


class TestCaseUserProduct(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path="D:/Python36/chromedriver.exe")
        self.wd.implicitly_wait(20)

    def test_user_product(self):
        wd = self.wd
        # 1) Otwórzcie stronę główną
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
        # 2) Kliknijcie na pierwszy towar w kategorii Campaigns
        first_product_element.click()
        product_title = wd.find_element(By.XPATH, "//*[@id='box-product']//h1[@class='title']").text
        # 3) Sprawdźcie, czy otwiera się strona właściwego towaru
        # Dokładniej, sprawdźcie, czy:
        # а) zgadza się tekst nazwy towaru
        assert first_product_name == product_title
        # Dokładniej, sprawdźcie, czy:
        # b) zgadza się cena (obie ceny)
        product_regularprice = wd.find_element(By.XPATH, "//*[@id='box-product']//s[@class='regular-price']")
        product_regularprice_color = product_regularprice.value_of_css_property("color")
        assert product_regularprice_color == 'rgba(102, 102, 102, 1)'
        # Oprócz tego, sprawdźcie style ceny na stronie głównej i na stronie towaru - pierwsza cena jest szara i przekreślona, a druga cena jest czerwona i pogrubiona.
        product_regularprice_strikethrough = product_regularprice.value_of_css_property("text-decoration")
        assert product_regularprice_strikethrough == 'line-through solid rgb(102, 102, 102)'
        product_regularprice_value = product_regularprice.text
        product_campaignprice = wd.find_element(By.XPATH, "//*[@id='box-product']//strong[@class='campaign-price']")
        product_campaignprice_color = product_campaignprice.value_of_css_property("color")
        assert product_campaignprice_color == 'rgba(204, 0, 0, 1)'
        # HINT: 1) "gray" is one that has the same values for the R, G and B channels in the RGBa representation, the "red" color is the one that has zero values for the G and B channels in the RGBa representation. It is necessary to get the color channels and compare these values on each page separately.
        assert Color.from_string(product_regularprice_color).red == Color.from_string(product_regularprice_color).green == Color.from_string(product_regularprice_color).blue
        assert Color.from_string(product_campaignprice_color).green == Color.from_string(product_campaignprice_color).blue == 0
        # HINT 3: 1) Please note, that You have to get the color channels and compare these values on each page separately.  From these lines: 'rgb (204, 0, 0, 1)' you have to get the channels, using the programming language.
        product_regularprice_color_rgba_list = product_regularprice_color[product_regularprice_color.find("(") + 1:product_regularprice_color.find(")")].split(", ")
        assert product_regularprice_color_rgba_list[0] == product_regularprice_color_rgba_list[1] == product_regularprice_color_rgba_list[2]
        product_campaignprice_color_rgba_list = product_campaignprice_color[product_campaignprice_color.find("(") + 1:product_campaignprice_color.find(")")].split(", ")
        assert product_campaignprice_color_rgba_list[1] == product_campaignprice_color_rgba_list[2] == '0'
        product_campaignprice_fontweight = product_campaignprice.value_of_css_property("font-weight")
        assert product_campaignprice_fontweight == '700'
        assert first_product_regularprice_value == product_regularprice_value
        product_campaignprice_value = product_campaignprice.text
        assert first_product_campaignprice_value == product_campaignprice_value
        # HINT: 2) In this task you should also check the font size, this is the "font-size" property --> not mentioned in polish translation, but I'll try guess which assertion were missing: product_regularprice_fontsize, product_campaignprice_fontsize
        assert product_regularprice.value_of_css_property("font-size") == '16px'
        assert product_campaignprice.value_of_css_property("font-size") == '22px'
        # + HINT 2) Font sizes should also be compared to each other as numbers, not as a string --> not mentioned in polish translation, but I'll try to fullfil your expectation
        assertint (''.join(filter(str.isdigit, product_regularprice.value_of_css_property("font-size")))) == 16
        assert int(''.join(filter(str.isdigit, product_campaignprice.value_of_css_property("font-size")))) == 22


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
