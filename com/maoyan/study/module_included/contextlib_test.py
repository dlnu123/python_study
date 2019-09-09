# contextlib
# __enter__
# __exit__
# @contextmanager
# @closing


from contextlib import contextmanager
from contextlib import closing
from urllib.request import urlopen


# __enter__/__exit__
class Query(object):

    def __init__(self, name):
        self.__name = name

    def __enter__(self):
        print("__enter__")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("__exit__ error")
        else:
            print("__exit__ end")

    def query(self):
        print("Query info about %s..." % self.__name)


q = Query("111")
q.query()
print("-------------------------------------")
with Query("222") as q:
    q.query()


print("-------------------------------------")
# @contextmanager
class Query1(object):

    def __init__(self, name):
        self.__name = name

    def query(self):
        print("Query info about %s..." % self.__name)


@contextmanager
def create_query(name):
    print("Begin")
    q = Query1(name)
    yield q
    print("End")


with create_query("test") as cq:
    cq.query()


print("-------------------------------------")


@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


with tag("h1"):
    print("hello")
    print("world")


# @closing
print("-------------------------------------")
with closing(urlopen("https://www.baidu.com")) as page:
    for line in page:
        print(line)
