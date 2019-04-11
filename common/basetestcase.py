from selenium import webdriver
import unittest
class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get('https://10.143.132.226:8441/BIMS6.0/')
        cls.driver.implicitly_wait(30)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()