import pytest
import allure

def test_attcat_text():
    allure.attach(body="这个是文本内容",name="文本",attachment_type=allure.attachment_type.TEXT)



def test_a