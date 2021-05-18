from qiyeweixin.page.add_member import AddMember
from qiyeweixin.page.base_page import BasePage


class Home(BasePage):
    def add_member(self):
        self.find("class","index_service_cnt_item").click()
        return AddMember(self._driver)