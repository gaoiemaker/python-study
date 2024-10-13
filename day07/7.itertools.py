# 通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列

import itertools

natuals = itertools.count(1)

ns = itertools.takewhile(lambda x: x <= 10, natuals)


# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器

a = [1, 2, 3]
b = [4, 5, 6]

c = a + b
# print(c)
# for c in itertools.chain(a, b):
#     print(c)


#  计算圆周率可以根据公式：


def pi(N):
    "计算pi的值"
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    ji = itertools.count(1, 2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    target = itertools.takewhile(lambda x: x <= 2 * N - 1, ji)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    res = 0
    for i, num in enumerate(target):
        res = res + (-1) ** i * 4 / num
    # step 4: 求和:
    return res


assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
