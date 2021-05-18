import yaml

from page.login_page import LoginPage
import pytest


def get_data():
    with open('../data/bi_data.yaml','r',encoding='UTF-8') as f:
        # data = yaml.load(f.read(),Loader=yaml.FullLoader)
        data = yaml.safe_load(f)
        dat = data['login_success']
        ids = data['ids']
    return [dat,ids]


class TestBi():

    def setup(self):
        self.d = LoginPage()

    def teardown(self):
        self.d.driver.quit()

    #测试登录成功
    # @pytest.mark.skip
    # @pytest.mark.parametrize("username,password",[("test2@qq.com",'123456')])
    @pytest.mark.parametrize("username,password",get_data()[0],ids=get_data()[1])
    def test_login(self,username,password):
        result = self.d.login(username,password).get_kanban()
        assert result =='基础看板'

    #测试登录失败
    # @pytest.mark.skip
    @pytest.mark.parametrize("username,password", [("test2@qq.com", '1234567'),
                                                   ("test@qq.com",'12345678')])
    def test_login_fail(self,username,password):
        result = self.d.login_fail_error(username,password)
        assert result == '登录失败'

    #测试密码输入过少
    # @pytest.mark.skip
    @pytest.mark.parametrize("username,password", [("test2@qq.com", '12345')])
    def test_login_password_less(self,username,password):
        result = self.d.login_password_less(username,password)
        assert result == '密码不能少于6位'

    #测试退出登录功能
    # @pytest.mark.skip
    @pytest.mark.parametrize("username,password",[("test2@qq.com",'123456')])
    def test_login_logout(self,username,password):
        result = self.d.login(username,password).logout().get_username()
        print(result)
        assert result =='登录'

    #测试跳转小时报表页面
    # @pytest.mark.skip
    @pytest.mark.parametrize("username,password", [("test2@qq.com", '123456')])
    def test_goto_huor_report(self,username,password):
        result = self.d.login(username,password).goto_hour_report().get_data()
        assert result =='项目'
