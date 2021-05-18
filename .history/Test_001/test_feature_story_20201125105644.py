import pytest
import allure


@allure.feature("登录模块")
class Test_Login:
    @allure.story("登录成功")
    def test_login_success(self):
        print("登录成功测试用例")
        pass
    @allure.story("登录失败")
    def test_login_success_a(self):
        print("登录失败")
        pass
    @allure.story("用户名缺失")
    def test_login_success_b(self):
        print("用户名缺失")
        pass
    @allure.story("密码缺失")
    def test_login_success_c(self):
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("")
        pass
