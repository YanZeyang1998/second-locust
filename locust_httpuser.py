import token

from locust import HttpUser, task, between
## 压力测试对象必须是HttpUser的之类, 程序启动后,扫描HttpUser子类,批量实例化这个类,每个实例都是一个虚拟用户模拟压力测试

## 1新造子类继承HttpUser
class myUser(HttpUser):
    wait_time = between(1, 3)
    ##def get_token(self):
            ##login_resp = self.client.get("/login", {"username": "admin", "password": ""})
            ##token = login_resp.json()["token"]
            ##self.token = token
            ##return token

##重写on_start方法,这样每个用户都有自己单独的token,每个虚拟用户实例化后都会执行一次on_start,所以重写这个函数用来拿token之类的前置操作
    def on_start(self):
        login_resp = self.client.get("/login", {"username": "admin", "password": ""})
        token = login_resp.json()["token"]
        self.token = token
    ##不用return

##task标记API为待压测对象,不用task装饰会跳过被测接口
    @task
    def test_run_api(self):
        headers={"Authorization": f"Bearer {self.token}"}
        body = {"username": "admin", "password": "","email": "","key":""}
        resp = self.client.post("/search", headers=headers, json=body)
        result = resp.json()
        assert resp.status_code == 200, f"ERROR--ERROR,{resp.status_code}"
        
print("dev1")
print("dev2")