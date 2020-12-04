# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time


class TestCaseAdminCountriesNewtab(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path="D:/Python36/chromedriver.exe")
        self.wd.implicitly_wait(20)

    def test_admin_countries_newtab(self):
        wd = self.wd
        wait = WebDriverWait(self.wd, 10)
        # 1)      Wejdź do panelu administracyjnego,
        wd.get("http://localhost/litecart/admin/login.php")
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys("admin")
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("admin")
        wd.find_element_by_name("login").click()
        # 2)      Otwórz pozycję menu Countries (lub stronę http://localhost/litecart/admin/?app=countries&doc=countries),
        wd.get("http://localhost/litecart/admin/?app=countries&doc=countries")
        # 3)      Otwórz edycję dowolnej strony lub rozpocznij tworzenie nowej,
        first_country_element = wd.find_element(By.CSS_SELECTOR, "a[title='Edit'")
        first_country_href = first_country_element.get_attribute("href")
        wd.get(first_country_href)
        # 4)      Przy niektórych polach znajdują się odnośniki w postaci kwadratowej ikony ze strzałką, które przekierowują na zewnętrzne strony. Sprawdź czy otwierają się one w nowym oknie. Oczywiście wystarczyłoby sprawdzić, czy link posiada atrybut target="_blank". Jednak, w tym zadaniu musisz kliknąć na link, aby się otworzył w nowym oknie, następnie przejść do tego okna, zamknąć go, wrócić i powtórzyć te czynności dla wszystkich tych linków. Nie zapomnij, że nowe okno nie otwiera się od razu, dlatego konieczne jest dodanie oczekiwania na jego otwarcie.
        fields_with_external_links_elements = wd.find_elements(By.XPATH, "//*[contains(@class,'external-link')]")
        main_window = wd.current_window_handle
        for element in fields_with_external_links_elements:
            old_windows = wd.window_handles
            element.click()
            # todo: how to orrectly enable method 'there_is_window_other_than'?
            new_window = wait.until(TestCaseAdminCountriesNewtab.there_is_window_other_than(self, old_windows))
            wd.switch_to.window(new_window)
            wd.close()
            wd.switch_to.window(main_window)
            time.sleep(2)

    def there_is_window_other_than(self, old_windows):
        wd = self.wd
        new_windows = wd.window_handles
        wait = WebDriverWait(wd, 10)
        wait.until(lambda d: len(old_windows) < len(new_windows))
        new_window = old_windows - new_windows
        return new_window

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
