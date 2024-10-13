# Base64是一种用64个字符来表示任意二进制数据的方法。 Python内置的base64可以直接进行base64的编解码

import base64

code_en =  base64.b64encode(b'noble')

code_url = base64.urlsafe_b64encode(b'abc++//--')

print(code_url)