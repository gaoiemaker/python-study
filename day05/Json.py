# 数据转化为json对象

import json

d = dict(name="noble", age=23)

j = json.dumps(d)


with open('./a.txt','wb') as f:
    job = json.dump(d,f)



# print(j)
# json 字符串反序列化 loads

json_str = '{"age": 20, "score": 88, "name": "Bob"}'

r = json.loads(j)

# print(r)

# json file-like Obj 反序列化 load
with open('./a.txt','rb') as f:
    p = json.load(f)
    print(p)
