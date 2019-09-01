# 操作文件和目录
#   os.name
#   os.uname
#   os.environ
#   os.environ.get('key')

#   os.path.abspath
#   os.path.join
#   os.mkdir
#   os.rmdir

#   os.path.split
#   os.path.splitext

#   os.rename
#   os.remove
import os, os.path


# 获取系统信息
print(os.name)
print(os.uname())
print(os.environ)
print(os.environ.get('PATH'))
print(os.environ.get('PATH1', 'null'))


# 目录操作（创建、删除）
print(os.path.abspath('.'))  # 查看当前目录的绝对路径
s = os.path.join('/Users/wangliang/PycharmProjects/python_study/com/maoyan/study/io', 'test')  # 在某个目录下创建一个新目录，首先生成目录的全路径
print(s)
print(os.mkdir(s))  # 创建目录
os.rmdir(s)  # 删除目录


# 目录拆分
print(os.path.split(s))  # 把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print(os.path.splitext(s))  # 把一个路径拆分为两部分，后一部分总是最后级别的文件扩展名（如果最后级别为文件夹，则后一部分为空字符串）


# 列举当前目录的所有文件夹
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 列举当前目录的所有文件
print([x for x in os.listdir('.') if os.path.isfile(x)])
# 列举当前目录的所有python文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

