# 使用stringio 在内存中读取
from io import StringIO

# f = StringIO()
# f.write('hello')
# f.write(' ')

# f.write('world!')

# print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    print(s)
    if s == '':
        break
    print(s.strip())