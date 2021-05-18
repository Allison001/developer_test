import pytest
import allure

def test_attcathtext():
    allure.attach(body="这个是文本内容",name="文本",attachment_type=allure.attachment_type.TEXT)



def test_attach_html():
    allure.attach("<body>这个是html文件</body>",name="HTML文件",attachment_type=allure.attachment_type.HTML)


def test_attach_picture():
    allure.attach.file("",name=,attachment_type=)
