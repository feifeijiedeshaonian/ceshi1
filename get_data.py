from operation_excel import OperationExcel
from data_config import GlobalBar
from operation_json import OperationJson


class GetData:

    def __init__(self):
        self.opera_excel = OperationExcel()
        self.gol_bar = GlobalBar()

    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 判断是否执行
    def get_is_run(self, row):
        col = int(self.gol_bar.get_run())
        run_model = self.opera_excel.get_cell_value(row, col)
        if run_model == "yes":
            flag = True
        else:
            flag = False
        return flag

    # 是否携带header
    def is_header(self, row):
        col = int(self.gol_bar.get_header())
        header = self.opera_excel.get_cell_value(row, col)
        if header == "yes":
            col1 = int(self.gol_bar.get_header_value())
            header_value = self.opera_excel.get_cell_value(row, col1)
            return header_value
        else:
            return None

    # 获取token
    def get_token(self, row):
        col = int(self.gol_bar.get_token())
        token = self.opera_excel.get_cell_value(row, col)
        return token

    # 获取请求方式
    def get_request_method(self, row):
        col = int(self.gol_bar.get_requset_way())
        requset_method = self.opera_excel.get_cell_value(row, col)
        return requset_method

    # 获取url
    def get_request_url(self, row):
        col = int(self.gol_bar.get_url())
        url = self.opera_excel.get_cell_value(row, col)
        return url

    # 获取请求数据
    def get_request_data(self, row):
        col = int(self.gol_bar.get_data())
        data = self.opera_excel.get_cell_value(row, col)
        return data

    # 通过关键字获取json数据
    def get_data_for_json(self, row):
        opera_json = OperationJson()
        data = self.get_request_data(row)
        if data == "none":
            return None
        else:
            request_data = opera_json.get_data(self.get_request_data(row))
            return request_data

    # 获取预期结果
    def get_expect_data(self, row):
        col = int(self.gol_bar.get_expect())
        expect = self.opera_excel.get_cell_value(row, col)
        if expect == "none":
            return None
        return expect

    def write_result(self, row, value):
        col = int(self.gol_bar.get_result())
        self.opera_excel.write_value(row, col, value)

    # 获取依赖的case
    def get_depend_key(self, row):
        col = int(self.gol_bar.get_data_depend())
        depent_key = self.opera_excel.get_cell_value(row, col)
        if depent_key == "":
            return None
        else:
            return depent_key

    # 判断是否有case依赖
    def is_depend(self, row):
        col = int(self.gol_bar.get_case_depend())
        depend_case_id = self.opera_excel.get_cell_value(row, col)
        if depend_case_id == "none":
            return None
        else:
            return depend_case_id

    # 从返回值中获取接口依赖字段的结果
    def get_depend_field(self, row):
        col = int(self.gol_bar.get_field_depend())
        data = self.opera_excel.get_cell_value(row, col)
        if data == "none":
            return None
        else:
            return data


if __name__ == "__main__":
    get_data = GetData()
    get_data.get_data_for_json(1)