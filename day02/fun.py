# 自定义函数 实现绝对值


def my_abs(num):
    if not isinstance(num, (int, float)):
        print(f"TypeError: the {num} is not int or float")

    else:
        if num > 0:
            return num
        else:
            return -num


res = my_abs("10")

print(res)

str = "hello %s" % "world"

print(str)
