# from selenium import webdriver
# import unittest
# class BimsTest(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Firefox()
#         cls.driver.implicitly_wait(30)
#         cls.driver.maximize_window()
#         cls.driver.get('https://10.143.132.226:8441/BIMS6.0/')
#         # cls.driver.implicitly_wait(30)
#         # cls.button = cls.driver.find_element_by_class_name('small-link')
#         # print("ok")
#         # cls.button.submit()
#     def test_bims(self):
#         self.account = self.driver.find_element_by_css_selector("div[class='Page-header center-block']>h2")
#         print('ok')
#         # self.account.send_keys('root')
#         # self.passwd = self.driver.find_element_by_id('password')
#         # self.passwd.send_keys('12345qwert!@#$%')
# if __name__=='__main__':
#     unittest.main()
def test(*args,**kwargs):
    print(*args)
a = [1,2]
test(*a)
test(a)

