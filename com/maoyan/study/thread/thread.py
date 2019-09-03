# 多线程
# _thread、threading
# lock
# GIL锁（Global Interpreter Lock）


import threading
import time
# thread %s is running...
# thread %s >>> %s
# thread %s ended.
# global balance


# 线程初探
# def loop():
#     print("thread %s is running..." % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n += 1
#         print("thread %s >>> %s" % (threading.current_thread().name, n))
#         time.sleep(1)
#     print("thread %s ended." % threading.current_thread().name)
#
#
# print("thread %s is running..." % threading.current_thread().name)
# thread = threading.Thread(target=loop, name="LoopThread")
# thread.start()
# thread.join()
# print("thread %s ended." % threading.current_thread().name)


# --------------------------------------------------------------------------------------
# 线程引发的资源竞争问题(下面的程序，最后的结果是否为0？)
balance = 0


def change_it(n):
    global balance
    balance += n
    balance -= n


def run_thread(n):
    for i in range(1000000):
        change_it(n)


t1 = threading.Thread(target=run_thread, args=(5,), name="t1")
t2 = threading.Thread(target=run_thread, args=(10,), name="t2")
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


# --------------------------------------------------------------------------------------
# 改善之后，是否为0
# balance = 0
# lock = threading.Lock()
#
#
# def change_it(n):
#     global balance
#     balance += n
#     balance -= n
#
#
# def run_thread(n):
#     for i in range(1000000):
#         try:
#             lock.acquire()
#             change_it(n)
#         finally:
#             lock.release()
#
#
# t1 = threading.Thread(target=run_thread, args=(5,), name="t1")
# t2 = threading.Thread(target=run_thread, args=(10,), name="t2")
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)
