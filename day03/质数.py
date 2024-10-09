# 输出质数的函数
def _old_list():
    n = 2
    while True:
        yield n
        n = n + 1


def is_symbal(n):
    return lambda x: x % n > 0


def printSymbol():
    lt = _old_list()
    while True:
        n = next(lt)
        yield n
        lt = filter(is_symbal(n), lt)


for i in printSymbol():
    if i <= 20:
        print(i)
    else:
        break
