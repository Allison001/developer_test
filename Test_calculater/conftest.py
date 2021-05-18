import pytest
import yaml

from Test_calculater.calculator import Calculator


@pytest.fixture(scope="class")
def get_add():
    print("获取测试函数")
    calc = Calculator()
    yield calc


with open("./datas.yaml") as f:
    datass = yaml.safe_load(f)
    add_data = datass["add_datas"]
    add_ids = datass["add_ids"]
@pytest.fixture(params=add_data,ids=add_ids)
def get_datas(request):
    print("获取测试数据")
    dat = request.param
    yield dat