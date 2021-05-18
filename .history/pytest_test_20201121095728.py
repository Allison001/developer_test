import pytest

class PyTestA:
    @pytest.mark.parametrze("a,b",[(10,20),(5,5)])
    def test_data1(self,a,b):
        print(a)

    # def test_data2(self):
    #     a = 5
    #     b = 5
    #     print(a+b)

    
ab = PyTestA()
ab.test_data1()