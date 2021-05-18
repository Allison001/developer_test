from selenium.webdriver import webdriver
import pytest
import allure
import time

def test_step_demo():
    dirver = webdriver.Chrome()