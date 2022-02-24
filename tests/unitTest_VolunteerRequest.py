import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class NCACMS_ATS16(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_nca(self):
        #login
        user = "smoorthi"
        pwd = "swethacse"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://ncavas.herokuapp.com")
        elem = driver.find_element_by_xpath("/html/body/nav/div/a").click()
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://ncavas.herokuapp.com")
        assert "Logged In"
        time.sleep(5)

        # find the ‘Volunteer Request’ and click it
        elem = driver.find_element_by_xpath("/html/body/div/div[1]/a[5]").click()
        time.sleep(2)
        continue_test = True
        time.sleep(2)
        #if test successful so far find 'View'
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr/td[5]/a").click()
        time.sleep(2)
        # find the ‘Volunteer Request’ and click it
        elem = driver.find_element_by_xpath("/html/body/div/div[1]/a[5]").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/nav/div/a").click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
