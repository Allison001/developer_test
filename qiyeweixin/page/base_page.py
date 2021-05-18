import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""
    def __init__(self,driver:WebDriver=None):
        browser_c = webdriver.ChromeOptions()
        browser_c.debugger_address ="127.0.0.1:9222"
        if driver is None:
            self._driver = webdriver.Chrome(options=browser_c)
        else:
            self._driver = driver
        self._driver.maximize_window()
        self._driver.implicitly_wait(10)
        if self._base_url != "":
            self._driver.get(self._base_url)


    def find(self,by,location):
        if by == "id":
            return self._driver.find_element_by_id(location)
        elif by == "class":
            return self._driver.find_element_by_class_name(location)
        elif by == "name":
            return self._driver.find_element_by_name(location)
        elif by == "xpath":
            return self._driver.find_element_by_xpath(location)
        elif by == "link_text":
            return self._driver.find_element_by_link_text(location)
        elif by == "partial":
            return self._driver.find_element_by_partial_link_text(location)
        elif by == "css":
            return self._driver.find_element_by_css_selector(location)
        elif by == "tag":
            return self._driver.find_element_by_tag_name(location)

    def find_a(self,by,location):
        return self._driver.find_element(by,location)


    def get_cookies(self):
        cookies = self._driver.get_cookies()
        with open("cookies.json","w") as f:
            json.dump(cookies,f)


    def add_cookies(self):
        # self._base_url = "https://work.weixin.qq.com/"
        with open("cookies.json","r") as f:
            cooks = json.load(f)
        for i in cooks:
            self._driver.add_cookie(i)
