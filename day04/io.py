# io流
# 流： 是单向的


# try:
#     f = open("./a.txt", "r")
#     print(f.read())
# except Exception as e:
#     print(e)
# finally:
#     if f:
#         f.close()

        
# 写入内容
with open("./a.txt", "a") as f:
    f.seek(0)
    print(f.write('\n窗前明月光'))
    #  print(f.write('疑是地上霜'))
    

# 使用语法糖
with open("./a.txt", "r") as f:
    print(f.readlines())
