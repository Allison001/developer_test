from qiyeweixin.page.main_page import Main


class Test_add_member:

    def setup(self):
        self.main = Main()

    def test_add_member(self):
        self.main.go_to_home().add_member().add_member_message()