# 使用byteIo 读写二进制

from io import BytesIO

f = BytesIO()

f.write('中文'.encode('utf-8'))

print(f.getvalue())