import json
import os


class OperationJson:

    def __init__(self, file_path=None):
        if file_path == None:
            # 获取当前文件路径
            current_path = os.path.abspath(__file__)
            # 获取当前文件的父目录
            father_path = os.path.dirname(current_path)
            path = os.path.join(father_path, "wenjian", "user.json")
            self.file_path = path
        else:
            self.file_path = file_path
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
            return data
    
    # 根据关键字获取数据
    def get_data(self, id):
        return self.data[id]

    # 写json
    def write_data(self, data):
        # 获取当前文件路径
        current_path = os.path.abspath(__file__)
        # 获取当前文件的父目录
        father_path = os.path.dirname(current_path)
        path = os.path.join(father_path, "wenjian", "cookie.json")
        with open(path, 'w') as fp:
            fp.write(json.dumps(data))


if __name__ == "__main__":
    opjson = OperationJson()
    print(opjson.get_data("login"))