from qiyeweixin.page.base_page import BasePage
from qiyeweixin.page.home_page import Home
from qiyeweixin.page.register_page import Register


class Login(BasePage):
    def go_to_register(self):
        self.find("class","login_registerBar_link").click()
        return Register(self._driver)
    def go_to_screen(self):
        return Home(self._driver)