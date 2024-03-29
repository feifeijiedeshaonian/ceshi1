# coding:utf-8
import xlrd
from xlutils.copy import copy
import os


class OperationExcel:

    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            # 获取当前文件路径
            current_path = os.path.abspath(__file__)
            # 获取当前文件的父目录
            father_path = os.path.dirname(current_path)
            path = os.path.join(father_path, "wenjian", "case1.xls")
            self.file_name = path
            self.sheet_id = 0
        self.data = self.get_data()

    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        # 获取sheet页的内容
        tables = data.sheets()[self.sheet_id]
        return tables

    # 获取单元格行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取单元格内容
    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)

    # 写入数据
    def write_value(self, row, col, value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)

    # 通过对应的case_id获取对应行的内容
    def get_rows_data(self, case_id):
        row_num = self.get_rows_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data

    # 通过对应的case_id获取对应的行号
    def get_rows_num(self, case_id):
        num = 0
        clols_data = self.get_cols_data()
        for col_data in clols_data:
            if case_id in col_data:
                return num
            num = num + 1
        
    # 根据行号找到该行的内容
    def get_row_values(self, row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    # 获取某一列的内容
    def get_cols_data(self, col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols

    

if __name__ == "__main__":
    operas = OperationExcel()
    print(operas.get_cell_value(1, 9))
    print(type(operas.get_cell_value(1, 9)))