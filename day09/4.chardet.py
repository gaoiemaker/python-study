import chardet

data = '最新の主要ニュース'.encode('euc-jp')
print(data.decode('euc-jp'))
info =  chardet.detect(data)

print(info)
# 使用chardet检测编码非常容易，chardet支持检测中文、日文、韩文等多种语言。