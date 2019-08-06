import requests
import json


class RunMethod():

    def get_main(self, url, data=None, headers=None):
        if data == "":
            res = requests.get(url=url, headers=headers)
        else:
            res = requests.get(url=url, data=data, headers=headers)
        return res.json()
    
    def post_main(self, url, data=None, headers=None):
        if data == "":
            res = requests.post(url=url, headers=headers)
        else:
            res = requests.post(url=url, data=data, headers=headers)
        return res.json()
    
    def run_main(self, method, url, data=None, headers=None):
        if method == "post":
            res = self.post_main(url, data, headers)
        else:
            res = self.get_main(url, data, headers)
        res = json.dumps(res)
        print(res)
        return res


if __name__ == "__main__":
    run = RunMethod()
    head = {
            "clientType": "app",
            "Content-Type": "application/x-www-form-urlencoded",
            "charset": "UTF-8"
            }
    run.run_main("get", "https://zhixin.zhiguaniot.com/api/app/login?username=13820921009&password=960811kai", "None", head)