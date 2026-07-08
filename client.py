import requests

class Client:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {"content-type": "application/json"}
        self.base_url = "http://127.0.0.1:8000"
        self.token = None

    def send(self,method,url,params=None,data=None,json=None,files=None,headers=None):
        url = self.base_url + url
        resp = self.session.request(url,params=params,data=data,json=json,files=files,headers=headers)
        return resp


client = Client()

