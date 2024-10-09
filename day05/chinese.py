# 中文序列化  使用ensure_ascii 后 中文会被转化成ask码 默认使用
import json

obj = dict(name="小明", age=18)

s = json.dumps(obj, ensure_ascii=False)

print(s)
