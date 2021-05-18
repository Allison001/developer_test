import requests


class Base():

    def __init__(self):
        #获取token
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww045168ae97ffe137&corpsecret=nv7UxbjQ7DoSSbfFsh8qhft0KrA-D8R5FgE0KARIvec"
        r = requests.get(url)
        self.token = r.json()["access_token"]
        #声明一个session
        self.s = requests.session()
        #将token添加到session中
        self.s.params = {"access_token":self.token}



    def req(self,*args,**kwargs):
        return self.s.request(*args,**kwargs).json()