# 文件读写
# 读文件
#   1、open（文件路径、读写模式、字符编码-encoding、错误处理-errors）
#       read()
#       read(size)
#       readline()
#       readlines()
#   2、with语法
# 写文件
# StringIO
# BytesIO
from io import StringIO, BytesIO


# /Users/wangliang/PycharmProjects/python_study/com/maoyan/study/io
try:
    f = open('/Users/wangliang/PycharmProjects/python_study/com/maoyan/study/io/read', 'r')
    print(f.read())
finally:
    f.close()


with open('/Users/wangliang/PycharmProjects/python_study/com/maoyan/study/io/read', 'r') as f:
    print(f.read())
    for line in f.readlines():
        print(line)


with open('/Users/wangliang/PycharmProjects/python_study/com/maoyan/study/io/read', 'r') as f:
    print("111")
    for line in f.readlines():
        print(line.strip())  # 去除最后的'\n'


with open('/Users/wangliang/PycharmProjects/python_study/com/maoyan/study/io/write', 'w') as fw:
    fw.write("I love yingying")


s = StringIO()
s.write('hello')
s.write(' ')
s.write('world')
print(s.getvalue())


f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    print(s.strip())
    if s == '':
        break


f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
