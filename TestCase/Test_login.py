from ddt import ddt,data,unpack
from selenium import webdriver
from common.base_page import BasePage
from common.file_read import File_read
import unittest
from Page.login_page import Login
from conf.setting import *
from Testdata import *
@ddt
class Test_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get('https://10.143.132.226:8441/BIMS6.0/')
        cls.driver.implicitly_wait(30)
    def test_login_page_validate(self):
        """
        测试页面的加载
        :return:
        """
        Login(self.driver)

    @data(*File_read('test.xlsx').excel_read('Sheet1'))
    @unpack
    def test_login_page_login(self, loginname, passwd):
        """
        测试页面的登录
        :param loginname:
        :param passwd:
        :return:
        """
        Login(self.driver).loggin(loginname,passwd)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__=="__main__":
    unittest.main(verbosity=2)