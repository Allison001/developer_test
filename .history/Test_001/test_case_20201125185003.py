import allure

@allure.link("https://www.baidu.com",name='链接')
def test_link():
    print("测试连接")

def test_case():
    print("")