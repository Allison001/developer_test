import time

from selenium.webdriver.common.by import By

from page.base_page import BasePage

#主页，为数据概率页面
from page.hour_report_page import HourReport


class Main(BasePage):

    #退出登录
    def logout(self):
        self.driver.find_element_by_css_selector('.is-round').click()
        from page.login_page import LoginPage
        return LoginPage(self.driver)

    #跳转到'小时报表页面'
    def goto_hour_report(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[1]/li/ul/div[2]/a/li').click()
        return HourReport(self.driver)

    #跳转到roi页面
    def goto_roi(self):
        pass

    #跳转到用户管理页面
    def goto_user_management(self):
        pass

    #跳转到权限管理页面
    def goto_authority_management(self):
        pass

    #跳转到角色管理页面
    def goto_role_management(self):
        pass

    #跳转到岗位管理页面
    def goto_post_management(self):
        pass
    #跳转到项目管理页面
    def goto_project_management(self):
        pass

    #获取'基础看板'文案
    def get_kanban(self):
        return self.find(By.CSS_SELECTOR,'.el-breadcrumb__inner').text

