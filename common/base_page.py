from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class BasePage(object):
    def __init__(self, driver=None):
        self.driver = driver
        self._validate_page()
        # self.cookies = cookieks

    def _validate_page(self):
        """验证页面是否登录成功"""
        pass

    def element_visible(self, by):
        """
        :param locat元祖类型:
        :return 定位元素对象:
        """
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by))
        return element
    def click(self, by):
        try:
            element = self.element_visible(by)
            element.click()
        except NoSuchElementException as e:
            print(e)

    def sendkeys(self, locat, text):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locat))
            element.send_keys(text)
        except NoSuchElementException as e:
            print(e)

    def is_tital(self,title):
        """
        根据页面标题，确定页面加载成功
        返回的element为bool值
        :return :
        """
        try:
            element = WebDriverWait(self.driver, 10).until(EC.title_is(title))
            return element
        except NoSuchElementException as e:
            raise e

    def element_visible2(self, by):
        try:
            return self.driver.find_element(*by)
        except NoSuchElementException as e:
            raise e

class InvalidPageException(Exception):
    """当未找到正确的页面时，抛出异常"""
    def __init__(self,massage):
        self.massage = massage
    def print(self):
        print(self.massage)