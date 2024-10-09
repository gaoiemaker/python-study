# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling

import pickle

d = dict(name="Bob", age=20, score=88)

e = pickle.dumps(d)

with open("./a.txt", "wb") as f:
    pickle.dump(d, f)
    f.close()

with open("./a.txt", "rb") as f:
    d = pickle.load(f)
    print(d)
    f.close()
