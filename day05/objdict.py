# 对象序列化
import json


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student("noble", 23)


js = json.dumps(stu, default=lambda obj: obj.__dict__)


def dict2stu(d) :
    return Student(d['name'],d['age'])

print(json.loads(js,object_hook=dict2stu))
