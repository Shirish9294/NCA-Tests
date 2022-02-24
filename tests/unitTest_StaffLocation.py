import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class NCACMS_ATS8(unittest.TestCase):

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
        #assert "Logged in"
        try:
            # attempt to find login, logged in
           elem = driver.find_element_by_xpath("/html/body/nav/div/a")
           assert True

        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False

        time.sleep(2)

        # find the ‘Locations’ and click it
        elem = driver.find_element_by_xpath("/html/body/div/div[1]/a[4]").click()
        time.sleep(2)
        continue_test = True
        time.sleep(1)
        # find the ‘Add Location’ and click it
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/span/a").click()
        time.sleep(2)
        continue_test = True
        time.sleep(1)
        # if test successful so far – set up the required inputs for a Staff
        if continue_test:
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/form/div/div/div[1]/div/input")
            elem.send_keys("NCA Association")
            elem =  driver.find_element_by_xpath("/html/body/div/div[2]/form/div/div/div[2]/div/input")
            elem.send_keys("1210 Seward plaza")
            driver.find_element_by_xpath("//*[@id='id_type']/option[2]").click()
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/form/div/div/div[4]/div/input")
            elem.send_keys("Lincon")
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/form/div/div/div[5]/div/input")
            elem.send_keys("Nebraska")
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/form/div/div/div[6]/div/input")
            elem.send_keys("6821")
            # elem = driver.find_element_by_xpath("/html/body/div/div[2]/form/div/div/div[7]/div/input[1]")
            # elem.send_keys("05/14/2021")
            # elem = driver.find_element_by_xpath("/html/body/div/div[2]/form/div/div/div[8]/div/input[1]")
            # elem.send_keys("10/14/2021")

            time.sleep(2)
            # click the Add button
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/form/div/div/button").click()
            time.sleep(2)
            # find the ‘View’ and click it
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr/td[7]/a").click()
            time.sleep(2)
            # find the ‘Edit’ and click it
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/p[1]/button/a").click()
            time.sleep(2)
            driver.find_element_by_id('id_city').clear()
            elem = driver.find_element_by_xpath("//*[@id='id_city']")
            elem.send_keys("Lincon")
            time.sleep(2)
            elem = driver.find_element_by_xpath("/html/body/div/div[2]/form/div/div/button").click()
            time.sleep(2)
            # find the ‘Delete’ and click it
            # elem = driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr/td[8]/a").click()
            # time.sleep(2)
            # driver.switch_to.alert.accept()
            # driver.find_element_by_xpath("/html/body/nav/div/a").click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
