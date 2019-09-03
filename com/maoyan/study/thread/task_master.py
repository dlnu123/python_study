# Master


import random
import queue
import time
from multiprocessing.managers import BaseManager


task_queue = queue.Queue()
result_queue = queue.Queue()


class QueueManager(BaseManager):
    pass


server_addr = '127.0.0.1'
QueueManager.register("get_task_queue", callable=lambda: task_queue)
QueueManager.register("get_result_queue", callable=lambda: result_queue)
manager = QueueManager(address=('127.0.0.1', 5000), authkey="abc".encode("utf-8"))
manager.start()

task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
    x = random.randint(0, 1000)
    print('Put task %d...' % x)
    time.sleep(1)
    task.put(x)
print('Try get results...')
for i in range(10):
    x = result.get()
    print('Result: %s' % x)
manager.shutdown()
print('master exit.')
