import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage
from page.main_page import Main


class LoginPage(BasePage):

    def login(self,username,password):
        self.find('name', 'username').send_keys(username)
        self.find('name','password').send_keys(password)
        self.find(By.CSS_SELECTOR,'.el-button--mini').click()

        # self.driver.find_element_by_name('username').send_keys(username)
        # self.driver.find_element_by_name('password').send_keys(password)
        # self.driver.find_element_by_css_selector('.el-button--mini').click()




        return Main(self.driver)

    def login_fail_error(self,username,password):

        # self.driver.find_element_by_name('username').send_keys(username)
        # self.driver.find_element_by_name('password').send_keys(password)
        # self.driver.find_element_by_css_selector('.el-button--mini').click()

        self.find('name','username').send_keys(username)
        self.find('name','password').send_keys(password)
        self.driver.find_element('css','.el-button--mini').click()

        #显示等待
        # def wait(x):
        #     return len(self.driver.find_elements_by_class_name('el-message__content')) == 1
        # WebDriverWait(self.driver,10).until(wait)

        #显示等待，转化为lambda表达式
        WebDriverWait(self.driver,10).until(lambda x:len(self.driver.find_elements_by_class_name('el-message__content')) == 1)

        #强制等待
        # time.sleep(3)
        #获取'登录失败'
        result = self.driver.find_element_by_class_name('el-message__content')
        #返回'登录失败'文案
        return result.text

    def login_password_less(self,username,password):
        # self.driver.find_element_by_name('username').send_keys(username)
        # self.driver.find_element_by_name('password').send_keys(password)
        # self.driver.find_element_by_css_selector('.el-button--mini').click()

        self.find('name','username').send_keys(username)
        self.find('name','password').send_keys(password)
        self.driver.find_element('css','.el-button--mini').click()

        #显示等待
        WebDriverWait(self.driver,10).until(lambda x:len(self.driver.find_elements_by_class_name('el-form-item__error')) ==1)
        # time.sleep(2)
        result = self.driver.find_element_by_class_name('el-form-item__error')
        return result.text

    def get_username(self):
        #获取'登录'文案
        result = self.find('css','.el-button--mini')
        return result.text