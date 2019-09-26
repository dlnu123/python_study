# asyncio.coroutine
# asyncio.sleep(1)
# asyncio.get_event_loop()
#   loop.run_until_complete(hello())
# asyncio.wait(tasks)
# asyncio.open_connection(host, 80)


import asyncio


@asyncio.coroutine
def hello():
    print("Hello world!")
    r = yield from asyncio.sleep(1)
    print(r)
    print("Hello world!")


loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()
