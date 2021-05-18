import allure

@allure.severity(allure.severity_level.BLOCKER)
def test_hight():
    print("这是一条最高级别的测试用例")

@allure.severity(allure.severity_level.CRITICAL)
def test_hight_1():
    print("这是一条严重级别的测试用例")


def test