import json

from selenium.webdriver.common.by import By

from qiyeweixin.page.base_page import BasePage
from qiyeweixin.page.home_page import Home
from qiyeweixin.page.login_page import Login
from qiyeweixin.page.register_page import Register


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/"
    def go_to_register(self):
        self.find("class","index_head_info_pCDownloadBtn").click()
        return Register

    def go_to_login(self):
        # self.find("class", "index_top_operation_loginBtn").click()
        self.find_a(By.XPATH,'//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        # self.find("xpath",'//*[@id="indexTop"]/div[2]/aside/a[1]')
        return Login(self._driver)

    def go_to_home(self):
        # self.get_cookies()

        self.find("xpath", '//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        # self.add_cookies()
        return Home(self._driver)