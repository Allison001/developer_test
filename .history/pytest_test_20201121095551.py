import pytest

class PyTestA:
    @pytest.mark.parametrze("a,b",[(),()])
    def test_data1(self):
        a = 10
        b = 20
        print(a+b)

    def test_data2(self):
        a = 5
        b = 5
        print(a+b)

    
ab = PyTestA()
ab.test_data2()