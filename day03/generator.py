# 迭代器


def gener():
    print(1)
    yield 1
    print(3)
    yield 3
    print(5)
    yield 5
    return 'done'

g = gener()

while True:
    try:
        x = next(g)
        print("f:",x)
    except StopIteration as e:
        print("迭代结束了：" + e.value)
        break
