# chardet


import chardet

print(chardet.detect(b'Hello, world!'))
print(chardet.detect(b'Hello, world!').get("encoding"))


data = "离离原上草，一岁一枯荣".encode("gbk")
print(chardet.detect(data))
data = "离离原上草，一岁一枯荣".encode("utf-8")
print(chardet.detect(data))
data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))
