import requests
import json


class RunMethod:

    def post_main(self, url, data=None, headers=None):
        if headers != None:
            res = requests.post(url=url, data=data, headers=headers)
        else:
            res = requests.post(url=url, data=data)
        return res.json()

    def get_main(self, url, data=None, headers=None):
        if headers != None:
            res = requests.get(url=url, data=data, headers=headers)
        else:
            res = requests.get(url=url, data=data)
        return res.json()
        
    def run_main(self, method, url, data=None, headers=None):
        if method == "post":
            res1 = self.post_main(url, data, headers)
        else:
            res1 = self.get_main(url, data, headers)
        res = json.dumps(res1, ensure_ascii=False, sort_keys=True, indent=2)
        return res
        
# json.dumps()函数是将一个Python数据类型列表进行json格式的编码（可以这么理解，json.dumps()函数是将字典转化为字符串）
# json.loads()函数是将json格式数据转换为字典（可以这么理解，json.loads()函数是将字符串转化为字典）
# Python encode() 函数用于将 Python 对象编码成 JSON 字符串。  demjson.encode(self, obj, nest_level=0)
# Python 可以使用 demjson.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型。


if __name__ == "__main__":
    run = RunMethod()
    head = {
            "clientType": "app",
            "Content-Type": "application/x-www-form-urlencoded",
            "charset": "UTF-8"
            }
    run.run_main("get", "https://zhixin.zhiguaniot.com/api/app/login?username=13820921009&password=960811kai", head)