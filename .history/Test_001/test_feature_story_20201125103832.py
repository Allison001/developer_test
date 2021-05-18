import pytest
import allure


@allure.feature("登录模块")
class Test_Login:
    # @allure.story("登录成功")
    def test_login_success(self):
        print("登录成功测试用例")
        pass
    
    def test_login_success_a(self):
        print("登录失败")
        pass

    def test_login_success_b(self):
        print("用户名缺失")
        pass

    def test_login_success_c(self):
        print("密码缺失")
        pass
