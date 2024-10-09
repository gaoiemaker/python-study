# 用于翻译的工具
# 写入阶段 先清空文件
with open("./res.txt", "w") as f:
    f.write('')
with open("./res.txt", "a") as res, open("./resours/origin.txt", "r") as origin, open("./resours/target.txt", "r") as target:
    while True:
        key = origin.readline().strip()
        value = target.readline().strip()
        if key and value:
            res.write(f"\"{key}\":\"{value}\",\n")
        elif key and not value:
            print("目标的内容少了")
        elif not key and value:
            print("翻译的内容少了")
        else:
            break

# 读取阶段
with open("./res.txt", "r") as f:
    while True:
        s = f.readline().strip()
        if not s:
            break
        print(s)
