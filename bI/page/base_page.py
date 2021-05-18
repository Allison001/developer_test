from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():

    def __init__(self,self_driver:webdriver=None):
        self_driver: WebDriver
        if self_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.get('http://52.80.62.62:8081/#/login?redirect=%2Fbasickanban%2Fdataoverview')
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
        else:
            self.driver = self_driver

    def find(self,by,*args,**kwargs):
        if by == "name":
            return self.driver.find_element(By.NAME,*args,**kwargs)
        elif by =='css':
            return self.driver.find_element(By.CSS_SELECTOR,*args,**kwargs)
        elif by =='xpath':
            return self.driver.find_element(By.XPATH,*args,**kwargs)
        elif by == 'classname':
            return self.driver.find_element(By.CLASS_NAME,*args,**kwargs)
        elif by == 'id':
            return self.driver.find_element(By.ID,*args,**kwargs)
        elif by == 'linktext':
            return self.driver.find_element(By.LINK_TEXT,*args,**kwargs)
        elif by == 'tagname':
            return self.driver.find_element(By.TAG_NAME,*args,**kwargs)
        elif by =='partlink':
            return self.driver.find_element(By.PARTIAL_LINK_TEXT,*args,**kwargs)
        else:
            return self.driver.find_element(by,*args,**kwargs)