import pytest
import allure

def test_attcathtext():
    allure.attach(body="这个是文本内容",name="文本",attachment_type=allure.attachment_type.TEXT)



def test_attach_html():
    allure.attach("<body>这个是html文件</body>",name="HTML文件",attachment_type=allure.attachment_type.HTML)


def test_attach_picture():
    allure.attach.file(source="https://exp-picture.cdn.bcebos.com/2a1ecb460596b814e9fce0b043d246fe464e2283.jpg?x-bce-process=image%2Fresize%2Cm_lfit%2Cw_500%2Climit_1",name="图片链接",attachment_type=allure.attachment_type.JPG)
