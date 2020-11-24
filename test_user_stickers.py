# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestCaseUserStickers(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path="D:/Python36/chromedriver.exe")
        self.wd.implicitly_wait(20)

    def test_user_stickers(self):
        wd = self.wd
        wd.get("http://localhost/litecart/")
        product_list = wd.find_elements(By.XPATH, "//li[contains(@class,'product')]")
        product_list_len = len(product_list)
        product_with_stickers_list = wd.find_elements(By.XPATH, "//div[contains(@class,'sticker')]")
        product_with_stickers_list_len = len(product_with_stickers_list)
        product_with_1sticker_list = wd.find_elements(By.XPATH, "//a/div[@class='image-wrapper']/img/following-sibling::div[count(preceding-sibling::*)+count(following-sibling::*)=1]")
        product_with_1sticker_list_len = len(product_with_1sticker_list)
        assert product_list_len >= product_with_stickers_list_len
        assert product_with_1sticker_list_len == product_with_stickers_list_len

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
