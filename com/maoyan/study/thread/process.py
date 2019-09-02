# 多进程(multiprocessing)

#   fork()
#   getppid()/getpid()
# multiprocessing -> Process
# multiprocessing -> Pool
# subprocess(控制子进程的输入和输出)--------subprocess.call、subprocess.Popen、communicate()
# multiprocessing -> Queue、Pipes(进程间通信)


import os
import time
import random
import subprocess
from multiprocessing import Process
from multiprocessing import Pool
from multiprocessing import Queue


# -----------------------------------------------------------------------------------------------------
# fork 相当于新建一个进程，去执行后面所有的代码
# 子进程永远返回 0
# 父进程则返回子进程的ID
# pid = os.fork()
# print("Process %s start..." % os.getpid())
# if pid == 0:
#     print("Child Process %s start...parent is %s" % (os.getpid(), os.getppid()))
# else:
#     print("Parent Process %s start..." % os.getpid())


# -----------------------------------------------------------------------------------------------------
# def func_sub(name):
#     print("Child Process %s start...pid = %s" % (name, os.getpid()))
#
#
# if __name__ == "__main__":
#     print("Parent process %s." % os.getpid())
#     process = Process(target=func_sub, args=("sub_process",))
#     print('Child process will start.')
#     process.start()
#     process.join()
#     print("Child process end.")


# -----------------------------------------------------------------------------------------------------
# def long_time_task(name):
#     print("Run task %s (%s)..." % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print("Task %s runs %0.2f seconds." % (name, end-start))
#
#
# if __name__ == '__main__':
#     print("Parent process %s." % os.getpid())
#     pool = Pool(4)
#     for i in range(6):
#         pool.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     # 调用 join() 之前必须先调用 close()
#     # 调用 close() 之后就不能继续添加新的 Process 了
#     pool.close()
#     pool.join()
#     print("All subprocesses done.")


# -----------------------------------------------------------------------------------------------------
# print('$ nslookup www.python.org')
# code = subprocess.call(('nslookup', 'www.python.org'))  # 可以是list，也可以是tuple
# print('Exit code:', code)


# print('$ nslookup')
# sub = subprocess.Popen(["nslookup"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, error = sub.communicate(b"set q=mx\npython.org\nexit\n")
# print(output.decode('utf-8'))
# print('Exit code:', sub.returncode)


# -----------------------------------------------------------------------------------------------------
# 进程之间通信
# def write(queue):
#     print("Process to write: %s" % os.getpid())
#     for x in ['A', 'B', 'C']:
#         print("Put %s to queue..." % x)
#         queue.put(x)
#         time.sleep(random.random() * 3)
#
#
# def read(queue):
#     print("Process to read: %s" % os.getpid())
#     while True:
#         x = queue.get()
#         print("Get %s from queue." % x)
#
#
# if __name__ == "__main__":
#     queue = Queue()
#     w = Process(target=write, args=(queue,))
#     r = Process(target=read, args=(queue,))
#     w.start()
#     r.start()
#     w.join()
#     r.terminate()
