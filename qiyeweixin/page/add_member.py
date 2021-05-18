from time import sleep

from selenium.webdriver.common.by import By

from qiyeweixin.page.base_page import BasePage


class AddMember(BasePage):
    def add_member_message(self):
        self.find("css",'#username').send_keys("zhang")
        self.find("css",'#memberAdd_english_name').send_keys("别名")
        return True