import pytest
import allure

def test_attcathtext():
    allure.attach(body="这个是文本内容",name="文本",attachment_type=allure.attachment_type.TEXT)



def test_attach_html():
    allure.attach("<body>这个是html文件</body>",name="HTML文件",attachment_type=allure.attachment_type.HTML)


def test_attach_picture():
    # allure.attach.file(source="https://www.zhifure.com/upload/images/2018/3/2716234168.jpg",name="图片链接",attachment_type=allure.attachment_type.JPG)
    allure.attach.file("./图片.jpg",name="图片链接",attachment_type=allure.attachment_type.JPG)
