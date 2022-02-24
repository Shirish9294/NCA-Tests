import unittest
import time
from idlelib import browser

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class NCACMS_ATS7(unittest.TestCase):

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

        # find the ‘Volunteers’ and click it
        elem = driver.find_element_by_xpath("/html/body/div/div[1]/a[5]").click()
        time.sleep(2)
        continue_test = True
        time.sleep(1)
        # find the ‘View’ and click it
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[1]/td[7]/a").click()
        time.sleep(2)
        # find the ‘Edit’ and click it
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/button[1]/a").click()
        time.sleep(2)
        # Enter Details
        driver.find_element_by_id('id_first_name').clear()
        elem = driver.find_element_by_xpath("//*[@id='id_first_name']")
        elem.send_keys("john")
        driver.find_element_by_id('id_last_name').clear()
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/form/div/div/div[2]/div/input")
        elem.send_keys("jones")
        driver.find_element_by_id('id_phone').clear()
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/form/div/div/div[4]/div/input")
        elem.send_keys("4163459834")
        driver.find_element_by_id('id_experience').clear()
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/form/div/div/div[5]/div/input")
        elem.send_keys("2years")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/form/div/div/button").click()
        time.sleep(2)
        # find the ‘Delete’ and click it
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[1]/td[8]/a").click()
        driver.switch_to.alert.accept()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/nav/div/a").click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
