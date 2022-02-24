import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class NCACMS_ATS11(unittest.TestCase):

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
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        driver.get("http://ncavas.herokuapp.com")
        time.sleep(2)
        # assert "Logged in"
        try:
            # attempt to find login, logged in
            elem = driver.find_element_by_xpath("/html/body/nav/div/a")
            assert True

        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False

        time.sleep(2)

        # find the ‘Notifications’ and click it
        elem = driver.find_element_by_xpath("/html/body/div/div[1]/a[8]").click()
        time.sleep(2)
        continue_test = True
        time.sleep(1)
        # find a ‘notification’ and click it
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/button[1]/a").click()
        time.sleep(2)
        # find the ‘Back to’ and click it
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/p/button/a").click()
        time.sleep(2)
        # driver.find_element_by_xpath("/html/body/nav/div/a").click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
