import requests

from test_api.api.base import Base


class MemberManager(Base):

    # #获取token
    # def __init__(self):
    #     url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww045168ae97ffe137&corpsecret=nv7UxbjQ7DoSSbfFsh8qhft0KrA-D8R5FgE0KARIvec"
    #     r = requests.get(url)
    #     self.token = r.json()["access_token"]

    #新增成员
    def add_member(self,userid:str,name:str,mobile:str,department:list,**kwargs):
        body = {
            "userid": userid,
            "name":name ,
            "mobile": mobile,
            "department": department}
        body.update(**kwargs)
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
        return self.req("post",url,json=body)

        # url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?"
        # return self.s.post(url,json=body).json()


    #查询成员
    def search_member(self,userid:str):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}"
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}"
        return self.req("get",url)


    #修改成员
    def updata_member(self,userid:str,name:str,mobile:str,department:list):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        body = {
            "userid": userid,
            "name":name ,
            "mobile": mobile,
            "department": department}
        return  self.req("post",url,json=body)

    #删除成员
    def delete_member(self,userid:str):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
        return self.req("get",url)



# a = MemberManager().add_member("zhangsant",name="张三t",mobile="159244641119",department=[1],gender="1")
# print(a)
# #
# # b = MemberManager().search_member(userid="zhangsanb")
# # print(b)
# #
# c = MemberManager().delete_member("zhangsant")
# print(c)