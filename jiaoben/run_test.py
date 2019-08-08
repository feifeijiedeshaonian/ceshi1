# coding:utf-8
from runmethod import RunMethod
from get_data import GetData
from common_util import CommonUtil
from dependent_data import DependentData
import json
from operation_header import OperationHeader
from operation_json import OperationJson
from send_email import send_main
import os


class RunTest:

    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()

    def go_on_run(self):
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                request_data1 = self.data.get_data_for_json(i)
                request_data = json.dumps(request_data1)
                expect = self.data.get_expect_data(i)
                header1 = self.data.is_header(i)
                header = eval(header1)
                token = self.data.get_token(i)
                depend_case = self.data.is_depend(i)
                if depend_case != None:
                    self.depend_data = DependentData(depend_case)
                    # 响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    # 获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    # 数据更新
                    request_data1[depend_key] = depend_response_data
                    request_data = json.dumps(request_data1)      
                if token == 'write':
                    res = self.run_method.run_main(method, url, request_data, header)
                    res = json.loads(res)
                    op_header = OperationHeader()
                    op_header.write_token(res["data"])
                    res = json.dumps(res)
                elif token == 'yes':
                    # 获取当前文件路径
                    current_path = os.path.abspath(__file__)
                    # 获取当前文件的父目录
                    father_path = os.path.dirname(current_path)
                    path = os.path.join(father_path, "wenjian", "cookie.json")
                    op_json = OperationJson(path)
                    token = op_json.get_data("access_token")
                    tokens = {'Authorization': "Bearer " + token}  
                    # 将header与token合并
                    header = dict(header, **tokens)
                res = self.run_method.run_main(method, url, request_data, header)
                if self.com_util.is_contain(expect, res):
                    self.data.write_result(i, "pass")
                    pass_count.append(i)
                else:
                    self.data.write_result(i, res)
                    fail_count.append(i)
        send_main(pass_count, fail_count)         


if __name__ == "__main__":
    run = RunTest()
    run.go_on_run()


