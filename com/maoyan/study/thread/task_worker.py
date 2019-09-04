# Worker


from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


QueueManager.register("get_task_queue")
QueueManager.register("get_result_queue")

print('Connect to server %s...' % "127.0.0.1")
manager = QueueManager(address=("127.0.0.1", 5000), authkey="abc".encode("utf-8"))
manager.connect()
task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
    n = task.get()
    m = n * n
    print('run task %d * %d...' % (n, n))
    result.put(m)
print('worker exit.')
