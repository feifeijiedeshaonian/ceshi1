from operation_excel import OperationExcel
from runmethod import RunMethod
from get_data import GetData
from jsonpath_rw import parse
import json
from operation_json import OperationJson


class DependentData:

    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel
        self.data = GetData()

    # 执行依赖测试获取结果
    def run_dependent(self):
        run_method = RunMethod()
        row_num1 = self.opera_excel()
        row_num = row_num1.get_rows_num(self.case_id)
        request_data1 = self.data.get_data_for_json(row_num)
        request_data = json.dumps(request_data1)
        header1 = self.data.is_header(row_num)
        header = eval(header1)
        method = self.data.get_request_method(row_num)
        url = self.data.get_request_url(row_num)
        token = self.data.get_token(row_num)
        if token == 'yes':
            op_json = OperationJson(r"E:\jiekoudata\cookie.json")
            token = op_json.get_data("access_token")
            tokens = {'Authorization': "Bearer " + token}  
            # 将header与token合并
            header = dict(header, **tokens)
        res = run_method.run_main(method, url, request_data, header)
        return json.loads(res)

    # 根据依赖的key去获取执行依赖测试case的响应，然后返回
    def get_data_for_key(self, row):
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependent()
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]
