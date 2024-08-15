import os
import pathlib
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Firefox()

class WebpageTests(unittest.TestCase):

    def test_title(self):
         driver.get(file_uri("counter.html"))
         self.assertEqual(driver.title, "Counter")

    def test_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element(By.ID, "add")
        display = driver.find_element(By.TAG_NAME, "h1")
        increase.click()
        self.assertEqual(display.text, "1")

    def test_decrease(self):
        driver.get(file_uri("counter.html"))
        decrease = driver.find_element(By.ID, "substract")
        display = driver.find_element(By.TAG_NAME, "h1")
        decrease.click()
        self.assertEqual(display.text, "-1")

    def test_multiple_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element(By.ID, "add")
        display = driver.find_element(By.TAG_NAME, "h1")
        for i in range(25):
            increase.click()
        self.assertEqual(display.text, "25")
    
    def test_input_text(self):
        driver.get(file_uri("counter.html"))
        text = driver.find_element(By.ID, "in-text")
        text.send_keys("Test 01")
        self.assertEqual(text.get_attribute("value"), "Test 01")

    def test_input_number(self):
        driver.get(file_uri("counter.html"))
        num = driver.find_element(By.ID, "in-num")
        num.send_keys("12345678")
        self.assertEqual(num.get_attribute("value"), "12345678")


if __name__ == "__main__":
    unittest.main()
