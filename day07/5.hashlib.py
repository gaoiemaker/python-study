# Python的hashlib提供了常见的哈希算法，如MD5，SHA1等等。 哈希算法就是通过哈希函数hash(data)对任意长度的数据data计算出固定长度的哈希digest
# 目的是为了发现原始数据是否被人篡改过 哈希算法之所以能指出数据是否被篡改过，就是因为哈希函数是一个单向函数，计算digest=hash(data)很容易，但通过digest反推data却非常困难。
# 而且，对原始数据做一个bit的修改，都会导致计算出的哈希完全不同。

import hashlib

md5 = hashlib.md5()  # 32位

md5.update("noble".encode("utf-8"))


sha1 = hashlib.sha1() # 40位

sha1.update("noblr".encode("utf-8"))
print(md5.hexdigest())

print(sha1.hexdigest())
# 任何哈希算法都是把无限多的数据集合映射到一个有限的集合中。这种情况称为碰撞
