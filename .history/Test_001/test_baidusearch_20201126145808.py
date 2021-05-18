"""
使用百度搜索pytest、unittest、allure,参数化，添加标记和步骤、打开浏览器后最大化、
搜索内容后截图放到测试用例里面
加入测试用例的地址
最后退出浏览器
"""

import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
import pytest
import time


@allure.feature("百度搜索功能")
def test_baidu_search():
    with allure.step("打开浏览器")：
        driver = webdriver.Chrome("./Applications/chromedriver")
        driver.get("https://www.baidu.com")


    driver.find_element_by_id("kw").send_keys("data")
    time.sleep(2)
    driver.find_element_by_id("su").click()
    time.sleep(2)

    driver.save_screenshot("./picture/a.png")
    allure.attach.file("./picture/a.png",name="图片链接",attachment_type=allure.attachment_type.PNG)
    driver.quit()