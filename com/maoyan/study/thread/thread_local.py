# ThreadLocal
# threading.local()


import threading
# Hello, %s (in %s)
thread_local = threading.local()


def process():
    s = thread_local.student
    print("Hello, %s (in %s)" % (s, threading.current_thread().name))


def run_thread(name):
    thread_local.student = name
    process()


t1 = threading.Thread(target=run_thread, args=("wangliang",), name="t1")
t2 = threading.Thread(target=run_thread, args=("yingying",), name="t2")
t1.start()
t2.start()
t1.join()
t2.join()



