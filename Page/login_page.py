from common.base_page import BasePage
from common.base_page import InvalidPageException
from selenium.webdriver.common.by import By
from Page.bims_home_page import Bims_home_page
class Login(BasePage):
    _login_logo = "div[class='Page-header center-block']>h2"
    _login_element = "div[class='from-group']>input[name='loginname']"
    _passwd_element = "div[class='from-group']>input[name='password']"
    _login_button = "button[class='btn  btn-primary']"

    def __init__(self,driver):
        super(Login, self).__init__(driver)

    def _validate_page(self):

        # self.driver.find_element_by_css_selector(self._login_logo)
        self.element_visible((By.CSS_SELECTOR, self._login_logo))

        # except Exception as e:
        #     print("页面元素不可见")
        #     return False
    def loggin(self,value,passwd):
        loger = self.element_visible(('css selector', self._login_element))
        password = self.element_visible(('css selector', self._passwd_element))
        button = self.element_visible(('css selector', self._login_button))
        try:
            loger.sendkeys(value)
            password.sendkeys(passwd)
            button.click()
            return Bims_home_page()
        except Exception as e:
            raise e
    def forget_passwd(self):

        pass
