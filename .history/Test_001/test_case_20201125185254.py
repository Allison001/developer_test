import allure

@allure.link("https://www.baidu.com",name='链接')
def test_link():
    print("测试连接")


@allure.testcase("https://www.baidu.com","测试用例地址链接")
def test_case():
    print("这个是测试用例地址")


def test_issue():
    print("这个bug地址链接")