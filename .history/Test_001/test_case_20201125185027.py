import allure

@allure.link("https://www.baidu.com",name='链接')
def test_link():
    print("测试连接")


@allure.testcase("https://www.baidu.com")
def test_case():
    print("测试用例地址")