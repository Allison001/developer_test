import pytest
import yaml
from Test_calculater.calculator import Calculator


def get_datas():
    with open("./datas.yaml") as f:
        data = yaml.safe_load(f)
        add_data = data["add_datas"]
        add_ids = data["add_ids"]
        return [add_data,add_ids]

class Test_calc:
    def setup_class(self):
        print("计算开始")

    def teardown_class(self):
        print("计算结束")

    def setup(self):
        self.calc = Calculator()
    def teardown(self):
        print("本次测试结束")

    @pytest.mark.parametrize("a,b,exp",get_datas()[0],ids=get_datas()[1])
    def test_add(self,a,b,exp):
        add = None
        try:
            add = self.calc.add(a,b)
            #处理有小数时，计算得出非常小的数，与期望值不一样
            if isinstance(add,float):
                add = round(add,2)
            print("结果：",add)
        except Exception as e:
            print(e)
        assert add == exp
