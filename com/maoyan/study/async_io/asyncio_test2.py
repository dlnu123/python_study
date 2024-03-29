import asyncio
import threading


@asyncio.coroutine
def hello():
    print("Hello world! (%s)" % threading.current_thread())
    r = yield from asyncio.sleep(1)
    print(r)
    print("Hello again! (%s)" % threading.currentThread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
