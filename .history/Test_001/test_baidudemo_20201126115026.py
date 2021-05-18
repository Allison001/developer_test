from selenium import webdriver
from selenium.webdriver import ActionChains
import pytest
import allure
import time

def test_step_demo():
    dirver = webdriver.Chrome("/Applications/chromedriver")
    dirver.get("https://www.baidu.com")

    dirver.find_element_by_id("kw").send_keys("pytest")
    time.sleep(2)
    dirver.find_element_by_id("su").click()
    time.sleep(2)

    dirver.save_screenshot("./result/1.jpg")
    allure.attach.file("./result/1.jpg",name="图片1",attachment_type=allure.attachment_type.JPG)
    allure.attach("<head></head><body>首页</body>","A")