# 使用os 操作文件和目录

import os

# print(os.uname())

# print(os.path.abspath('.'))

# 获取新目录路径

# dirpath = os.path.join('/Users/gaoshang/Desktop/python-study','textdir') 

# 新建目录
# os.mkdir(dirpath)


# 删除目录 
# os.rmdir(dirpath)


# 获取文件名

# print(os.path.split(os.path.abspath('.') + '/a.txt'))
# print(os.path.splitext(os.path.abspath('.') + '/a.txt'))

# 文件操作 重命名 和 删除 创建

# os.rename('a.txt','b.txt')

# os.remove('b.txt')

# 列出文件目录

arr =  [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(arr)