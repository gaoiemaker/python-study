import requests

r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json') # 豆瓣首页
print(r.status_code)

print(r.text)