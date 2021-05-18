from selenium import webdriver
from selenium.webdriver import ActionChains
import pytest
import allure
import time

def test_step_demo():
    dirver = webdriver.Chrome("/Applications/chromedriver")
    dirver.get("https://www.baidu.com")

    