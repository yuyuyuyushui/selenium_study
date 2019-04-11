from common.base_page import BasePage
class Bims_home_page(BasePage):
    _home_log = "span[class='logo-lg']"
    def __init__(self,driver):
        super(Bims_home_page,self).__init__(driver)
    def _validate_page(self):
        pass