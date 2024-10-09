# 二元一次方程求解
import math


# ax**2 + bx + c = 0
def quadratic(a, b, c):
    if b**2 - 4 * a * c > 0:
        return -b + math.sqrt(b**2 - 4 * a * c), -b - math.sqrt(b**2 - 4 * a * c)
    elif b**2 - 4 * a * c == 0:
        return -b + math.sqrt(b**2 - 4 * a * c)
    else:
        print("此方程无解")
        return ()


res = quadratic(1, 2, -3)
# print(res)


# ax+by  = c   dx+ey  = f
def dou_quadratic(a, b, c, d, e, f):
    # y = (dc - af) / (bd -ae)
    # x = c - b(dc - af)/(bd- ae)

    return c - b * (d * c - a * f) / (b * d - a * e), (d * c - a * f) / (b * d - a * e)

res2 = dou_quadratic(1,1,20,2,4,60)
print(res2)