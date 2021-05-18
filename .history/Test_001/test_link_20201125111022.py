
import allure

@allure.link("https://www.baidu.com",name="链接地址")
def test_link_a():
    print("测试连接的测试用例")


testcase="https://www.baidu.com"
@allure.testcase(testcase,"测试用例地址")
def test_testcase():
    print("这个是测试用例地址")


def test_issue()