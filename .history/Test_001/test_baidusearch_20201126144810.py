"""
使用百度搜索pytest、unittest、allure,参数化，添加标记和步骤、打开浏览器后最大化、
搜索内容后截图放到测试用例里面
加入测试用例的地址
"""

import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
import pytest


def test_baidu_search():
    driver = webdriver.Chrome("./Applications/chromedriver")
    driver.get("https://www.baidu.com")


    driver.find_element_by_id("kw").send_keys("")