import json
from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
headers = {'Origin': 'https://passport.weibo.cn', 'User-Agent': 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25', 'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F'}

def fetch_data(url):
    req = request.Request(url)
    for k, v in headers.items():
        req.add_header(k, v)
    with request.urlopen(req) as f:
        js_data = f.read().decode('utf-8')
        Python_data = json.loads(js_data)
        return Python_data

# 测试
URL = 'http://www.httpbin.org/get'
data = fetch_data(URL)
print(data)
# assert data['origin'] == '103.151.173.102'  #这里是自己的IP地址
# print('ok')