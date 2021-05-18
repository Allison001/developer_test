import allure

@allure.severity(allure.severity_level.BLOCKER)
def test_hight():
    print("这是一条最高级别的测试用例")

@allure.severity(allure.severity_level.CRITICAL)
def test_hight_1():
    print("这是一条严重级别的测试用例")

@allure.severity(allure.severity_level.NORMAL)
def test_hight_2():
    print("这是一条正常级别的测试用例")

@allure.severity(allure.severity_level.MINOR)
def test_hight_3():
    print("这是一条不验证的测试用例")


def test_hight_4():
    print("这是一条轻微的测试yob")