import pytest

from test_api.api.member_manger import MemberManager


class TestMember():
    def setup(self):
        self.managerzz = MemberManager()


    @pytest.mark.parametrize("userid,name,mobile,department,gender",
                             [("wangwu002", "张一", "15910720001", [1],"1"),
                              ("wangwu003", "张儿", "15910720002", [2],"1"),
                              ("wangwu004", "张思", "15910720003", [2],"2")])
    def test_add_member(self,userid,name,mobile,department,gender):
        #清除用户
        a = self.managerzz.delete_member(userid)
        print(a)

        #新增用户
        r = self.managerzz.add_member(userid=userid, name=name, mobile=mobile, department=department,gender=gender)
        print(r)

        #查询用户
        r1 = self.managerzz.search_member(userid)

        print(r1)
        assert r1["name"] == name


    @pytest.mark.parametrize("userid",[("wangwu002"),("wangwu003"),("wangwu004")])
    def test_delete_member(self,userid):
        #清除用户
        self.managerzz.delete_member(userid=userid)
        #查询用户不存在
        r = self.managerzz.search_member(userid)
        assert r["errcode"] == 60111



