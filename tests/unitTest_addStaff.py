# # automated unit test to ensure a window to add a new client appears
# when the "+ New" button is clicked
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class NCACMS_ATS2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_nca(self):
        # login from the admin pane
        user = "smoorthi"
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
        elem.send_keys(Keys.RETURN)
        driver.get("http://ncavas.herokuapp.com")
        assert "Logged In"
        time.sleep(3)
        # find the ‘Add Staff’ and click it
        driver.find_element_by_xpath("/html/body/div/div[1]/a[2]").click()
        time.sleep(3)
        continue_test = True
        time.sleep(2)
        # if test successful so far – set up the required inputs for a Staff
        if continue_test:
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/form/div[1]/div/input")
            elem.send_keys("Johnpetes")
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/form/div[2]/div/input")
            elem.send_keys("john@gmail.com")
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/form/div[3]/div/input")
            elem.send_keys("NcaLogin123")
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/form/div[4]/div/input")
            elem.send_keys("NcaLogin123")
            time.sleep(4)
            # click the Signup button
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/form/button").click()
            time.sleep(4)

            driver.find_element_by_xpath("/html/body/nav/div/a").click()
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
