import xlrd
from xlutils import copy


class OperationExcel():

    def __init__(self, file_path, sheet_id):
        if file_path:
            self.file_path = file_path
            self.sheet_id = sheet_id
        else:
            self.file_path = ""
            self.sheet_id = 0
        self.data = self.read_excel()

    def read_excel(self):
        table = xlrd.open_workbook(self.file_path)
        data = table.sheets()[self.sheet_id]
        return data

    def get_lines(self):
        return self.data.nrows

    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)

    def copy_data(self, row, col, value):
        read_data = xlrd.open_workbook(self.file_path)
        write_data = read_data.copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.file_path)
