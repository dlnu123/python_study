# psutil


import psutil


# 获取CPU信息
print(psutil.cpu_count())  # CPU逻辑数量
print(psutil.cpu_count(False))  # CPU物理核心
print(psutil.cpu_times())
for x in range(3):
    print(psutil.cpu_percent(interval=1, percpu=True))
print("-------------------------------------------------------------------")


# 获取内存信息
print(psutil.virtual_memory())  # 获取物理内存信息
print(psutil.swap_memory())  # 获取交换内存信息
print("-------------------------------------------------------------------")


# 获取磁盘信息
print(psutil.disk_partitions())
print(psutil.disk_usage('/'))
print(psutil.disk_io_counters())
print("-------------------------------------------------------------------")


# 获取网络信息
print(psutil.net_io_counters())
print(psutil.net_if_addrs())
print(psutil.net_if_stats())
# print(psutil.net_connections())
print("-------------------------------------------------------------------")


# 获取进程信息
print(psutil.pids())
print(psutil.Process(15246).name())
