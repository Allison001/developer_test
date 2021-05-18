import requests


class Base():
    #获取token
    def __init__(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww045168ae97ffe137&corpsecret=nv7UxbjQ7DoSSbfFsh8qhft0KrA-D8R5FgE0KARIvec"
        r = requests.get(url)
        self.token = r.json()["access_token"]

        #声明一个sess
        self.s = requests.session()
        #讲token添加到session中
        self.s.params = {"access_token":self.token}


    def req(self,method, url,**kwargs):
        return self.s.request(method, url,**kwargs)
