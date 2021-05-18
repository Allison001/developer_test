import requests

from test_api2.api.base import Base


class AddManager(Base):

    def add_member(self,userid,name,mobile,department,**kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        payload = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department": department}
        payload.update(**kwargs)
        return self.req(method="post",url=url,json=payload).json()


    def search_member(self,userid):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}"
        return self.req("get",url=url).json()

    def updata_member(self,userid,name,mobile,department,**kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        payload = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department": department}
        payload.update(**kwargs)
        return self.req(method="post",url=url,json=payload).json()


    def delete_member(self,userid):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?&userid={userid}"
        return self.req("get",url=url).json()


# a = AddManager().add_member("zhangsana",'张三a','13800000001',[1,2],gender="1")
# print(a)

# s = AddManager().search_member("zhangsana")
# print(s)
#
# u = AddManager().updata_member("zhangsana","张三",'13800000002',[1],gender="2")
# print(u)
#
# s = AddManager().search_member("zhangsana")
# print(s)

# b = AddManager().delete_member("zhangsana")
# print(b)