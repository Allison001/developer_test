import pytest
import yaml


class Test_data():

    @pytest.mark.parametrize("env",yaml.safe_load(open('./daya1.yaml')))
    def test_env(self,env):
        if "test" in env:
            print("这是测试环境")
            print(env["test"])
        elif "dev" in env:
            print("这是正式环境")
            print(env['dev'])
        else:
            print("啥也不是")

