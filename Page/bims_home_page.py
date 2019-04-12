from common.base_page import BasePage
from Page.son_page.current_online_user_query import *
class Bims_home_page(BasePage):
    _home_log = "span[class='logo-lg']"
    def __init__(self):
        super(Bims_home_page,self).__init__()
        self.Current_Online_User_Query = Current_Online_User_Query()
    def _validate_page(self):
        pass
