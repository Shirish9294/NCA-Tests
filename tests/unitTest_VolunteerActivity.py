import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class NCACMS_ATS13(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_nca(self):
        user = "Jaswinder"
        pwd = "swethacse"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://ncavas.herokuapp.com")
        elem = driver.find_element_by_xpath("/html/body/nav/div/a").click()
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        driver.get("http://ncavas.herokuapp.com")
        time.sleep(2)
        assert "Logged in"
        try:
            # attempt to find login, logged in
           elem = driver.find_element_by_xpath("/html/body/nav/div/a")
           assert True

        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False

        time.sleep(2)

        # find the ‘Activities’ and click it
        elem = driver.find_element_by_xpath("/html/body/div/div[1]/a[3]").click()
        time.sleep(2)
        continue_test = True
        time.sleep(1)
        # find the ‘Add Activity’ and click it
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/span/a").click()
        time.sleep(2)
        continue_test = True
        time.sleep(1)
        # if test successful so far – set up the required inputs
        if continue_test:
            driver.find_element_by_xpath("//*[@id='id_volunteer']/option[2]").click()
            driver.find_element_by_xpath("//*[@id='id_victim']/option[2]").click()
            driver.find_element_by_xpath("//*[@id='id_location']/option[2]").click()
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/div/div[4]/div/input")
            elem.send_keys("V-Activity-111")
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/div/div[5]/div/input")
            elem.send_keys("Consulting")
            driver.find_element_by_xpath("//*[@id='id_type']/option[1]").click()
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/div/div[7]/div/input[1]")
            elem.send_keys("05/04/2021 10:20 AM")
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/div/div[8]/div/input[1]")
            elem.send_keys("05/14/2021 11:20 AM")
            elem = driver.find_element_by_xpath("//*[@id='id_notes']")
            elem.send_keys("Consulting patient")

            time.sleep(2)
            # click the Add button
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/button").click()
            time.sleep(2)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
