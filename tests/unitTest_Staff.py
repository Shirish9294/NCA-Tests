import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class NCACMS_ATS4(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_nca(self):
        user = "Shirish"
        pwd = "swethacse"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://ncavas.herokuapp.com")
        elem = driver.find_element_by_xpath("/html/body/nav/div/a").click()
        time.sleep(3)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        driver.get("http://ncavas.herokuapp.com")
        time.sleep(3)
        assert "Logged in"

        # find the ‘Staff’ and click it
        driver.find_element_by_xpath("/html/body/div/div[1]/a[2]").click()
        time.sleep(2)
        continue_test = True
        time.sleep(2)
        #if test successful so far view Staff details
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/button/a").click()
        time.sleep(2)
        continue_test = True
        time.sleep(2)
        # if test successful so far Enter Staff details
        if continue_test:
            driver.find_element_by_id('id_first_name').clear()
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/form/div/div/div[1]/div/input")
            elem.send_keys("Shirish")
            driver.find_element_by_id('id_last_name').clear()
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/form/div/div/div[2]/div/input")
            elem.send_keys("Srinivasa")
            driver.find_element_by_id('id_email').clear()
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/form/div/div/div[3]/div/input")
            elem.send_keys("shirishn94@gmail.com")
            driver.find_element_by_id('id_phone').clear()
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/form/div/div/div[4]/div/input")
            elem.send_keys("4025974039")  # use default value
            time.sleep(2)
            #click the Update button
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/form/div/div/button").click()
            time.sleep(2)
            # if test successful so far view Staff details
            elem = driver.find_element_by_xpath("/html/body/div/div[1]/a[2]").click()
            time.sleep(2)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
