import os
 
# 获取当前文件路径
current_path = os.path.abspath(__file__)
# 获取当前文件的父目录
father_path = os.path.dirname(current_path)
path = os.path.join(father_path, "log", "runlog.log")
print('当前目录:' + current_path)
print('当前父目录:' + father_path)
print(path)
 