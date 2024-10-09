def triangles(max):
    l = [1]
    n = 0
    while n < max:
        yield l
        m = l
        for i in range(0, len(m) - 1):
            if i == 0:
                l = [1]    
            l.append(m[i] + m[i + 1])
        l.append(1)
        n = n + 1
    return "done"


for i in triangles(20):
    print(i)
