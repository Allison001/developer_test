import pytest

class Test_A:
    @pytest.mark.parametrize('a,b',[(10,20),(5,5)])
    def test_data1(self,a,b):
        print(a + b)

    def test_data2(self):
        a = 5
        b = 5
        print(a+b)

if __name__ == '__main__':
    pytest.main
    