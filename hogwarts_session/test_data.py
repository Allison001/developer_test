import pytest
import yaml

# a = yaml.safe_load(open('/Users/yeahmobi/Desktop/work/python/developer/hogwarts_session/daya2.yaml'))
# print(a)

class TestData():

    @pytest.mark.parametrize("a,b",yaml.safe_load(open('./daya2.yaml')),ids=["one","two","three"])
    def test_data(self,a,b):
        print(a+b)