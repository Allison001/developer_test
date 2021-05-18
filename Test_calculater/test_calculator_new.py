

class Test_calc:

    # @pytest.mark.parametrize("a,b,exp",[(1,2,3)])
    def test_add(self,get_add,get_datas):
        add = None
        try:
            add = get_add.add(get_datas[0],get_datas[1])
            print(add)
            if isinstance(add,float):
                add = round(add,2)
        except Exception as e:
            print(e)
        assert add == get_datas[2]


