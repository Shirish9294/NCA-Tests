import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class NCACMS_ATS18(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_nca(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://ncavas.herokuapp.com")
        elem = driver.find_element_by_xpath("/html/body/div/nav/div/ul/li/a").click()
        time.sleep(3)
        #Fill out the details
        elem = driver.find_element_by_xpath("/html/body/div/div/form/div[1]/div/input")
        elem.send_keys("Mona")
        elem = driver.find_element_by_xpath("/html/body/div/div/form/div[2]/div/input")
        elem.send_keys("Prakash")
        elem = driver.find_element_by_xpath("/html/body/div/div/form/div[3]/div/input")
        elem.send_keys("1110 S 64st")
        elem = driver.find_element_by_xpath("/html/body/div/div/form/div[4]/div/input")
        elem.send_keys("Omaha")
        elem = driver.find_element_by_xpath("/html/body/div/div/form/div[5]/div/input")
        elem.send_keys("Nebraska")
        elem = driver.find_element_by_xpath("/html/body/div/div/form/div[6]/div/input")
        elem.send_keys("987654321")
        elem = driver.find_element_by_xpath("/html/body/div/div/form/div[7]/div/input")
        elem.send_keys("Pmona@gmail.com")
        elem = driver.find_element_by_xpath("/html/body/div/div/form/div[8]/div/input")
        elem.send_keys("683005")
        elem = driver.find_element_by_xpath("/html/body/div/div/form/div[9]/div/input")
        elem.send_keys("Blood cancer")

        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/form/button").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()