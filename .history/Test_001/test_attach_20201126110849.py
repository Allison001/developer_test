import pytest
import allure

def test_attcathtext():
    allure.attach(body="这个是文本内容",name="文本",attachment_type=allure.attachment_type.TEXT)



def test_attach_html():
    allure.attach("<body>这个是html文件</body>",name="HTML文件",attachment_type=allure.attachment_type.HTML)


def test_attach_picture():
    allure.attach.file(source="https://www.google.com/url?sa=i&url=https%3A%2F%2F699pic.com%2Ftupian%2Fyueliang.html&psig=AOvVaw3beZRSpEfjjlGrYY5TQ6LT&ust=1606446522177000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCIimz-Sdn-0CFQAAAAAdAAAAABAD",name=,attachment_type=)
