import pytest
import yaml

from test_api2.api.add_manager import AddManager


def get_data():
    with open('/Users/yeahmobi/Desktop/work/python/developer/test_api2/data/add_manager_data.yaml') as f:
        a = yaml.safe_load(f)
        adds = a["adds"]
        uid = a["userid"]
        print(adds)
        return [adds,uid]


class TestMember():
    def setup(self):
        self.mem = AddManager()

    def teardown(self):
        pass

    @pytest.mark.parametrize("userid,name,mobile,department,gender",get_data()[0])
    def test_addmember(self,userid,name,mobile,department,gender):
        #清理数据
        self.mem.delete_member(userid)
        #添加数据
        self.mem.add_member(userid,name,mobile,department,gender=gender)
        #查询数据
        self.mem.search_member(userid)


    @pytest.mark.parametrize("userid",get_data()[1])
    def test_delete_menber(self,userid):
        #删除数据
        self.mem.delete_member(userid)
        #查询数据
        self.mem.search_member(userid)
