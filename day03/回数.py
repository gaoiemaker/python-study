def num_list(max):
    n = 0
    while n < max:
        yield n
        n = n + 1


def is_revice():
    return lambda x: (x > 10) and (str(x) == str(x)[::-1])


def get_revice(max):
    lt = num_list(max)
    lt = filter(is_revice(), lt)
    for i in lt:
        yield i


for i in get_revice(1000):
    if i < 1000:
        print(i)
    else:
        break
