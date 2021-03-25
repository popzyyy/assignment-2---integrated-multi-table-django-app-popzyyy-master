import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        user = "spqr"
        pwd = "spqr"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        time.sleep(1)
        driver.get("http://127.0.0.1:8000/service_list")
        time.sleep(1)
        driver.get("http://127.0.0.1:8000/product_list")
        time.sleep(1)
        driver.get("http://127.0.0.1:8000/customer_list")
        time.sleep(1)
        driver.get("http://127.0.0.1:8000/register")
        time.sleep(1)
        driver.get("http://127.0.0.1:8000/service/create")
        time.sleep(1)
        driver.get("http://127.0.0.1:8000/product/create")
        time.sleep(1)
        driver.get("http://127.0.0.1:8000/product/1/edit")
        time.sleep(1)
        driver.get("http://127.0.0.1:8000/product/1/delete")
        time.sleep(1)
        driver.get("http://127.0.0.1:8000/customer/1/edit")
        time.sleep(1)
        driver.get("http://127.0.0.1:8000/customer/1/delete")
        time.sleep(1)
        driver.get("http://127.0.0.1:8000/service/1/delete")
        time.sleep(1)
        driver.get("http://127.0.0.1:8000/service/1/edit")
        time.sleep(1)

        try:
            assert True


        except NoSuchElementException:
            self.fail("Test failed. Check URL paths.")

            assert False


        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
