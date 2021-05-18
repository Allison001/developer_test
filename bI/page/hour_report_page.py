from selenium.webdriver.common.by import By

from page.base_page import BasePage


class HourReport(BasePage):

    #获取日期文案
    def get_data(self):
        result = self.find(By.CSS_SELECTOR,'.el-form-item__label')
        return result.text
