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
import yaml

@allure.testcase("https://github.com/Allison001/test_demo",name="测试用例地址")
@allure.feature("百度搜索功能")
@pytest.mark.parametrize('data',yaml.safe_load(open("./data/data_baidusearch.yaml")))
def test_baidu_search(data):
    with allure.step("打开浏览器"):
        driver = webdriver.Chrome("/Applications/chromedriver")
        driver.get("https://www.baidu.com")

    with allure.step("浏览器最大化"):
        driver.maximize_window()

    with allure.step(f"搜索框内输入{data}"):
        driver.find_element_by_id("kw").send_keys(data)
        time.sleep(2)
    
    with allure.step("点击搜索按钮"):
        driver.find_element_by_id("su").click()
        time.sleep(2)

    with allure.step("截取图片"):
        driver.save_screenshot(f"./picture/.png")

    with allure.step("将图片放到测试用例里面"):
        allure.attach.file("./picture/a.png",name="图片链接",attachment_type=allure.attachment_type.PNG)

    with allure.step("退出浏览器"):
        driver.quit()