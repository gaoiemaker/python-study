#  @contextmanager
from contextlib import contextmanager

class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)
        
# 经过@contextmanager装饰的generator  它的作用就是把任意对象变为上下文对象，并支持with语句。
@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')    

with create_query('Bob') as q:
    q.query()
    