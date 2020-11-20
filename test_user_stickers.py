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
        stickers_list = wd.find_elements(By.XPATH, "//div[contains(@class,'sticker')]")
        stickers_list_len = len(stickers_list)
        wd.implicitly_wait(20)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
