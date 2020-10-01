import  functools
import time
def print_run_time(func):
    @functools.wraps(func) 
    def wrapper(*args,**kw):
        local_time=time.time()
        func(*args,**kw)
        t=time.time()-local_time
        print(t)
    return wrapper
 
@print_run_time
def test(x):
    for i in range(1000):
        print(x,end='')
    print('\n')
    return x
 
test(1)


import functools
import time

def printRunTime(func):
    @functools.wraps(func)
    def wrapper(*arg, **kw):
        print(time.time())
        func(*arg, **kw)
    return wrapper

@printRunTime
def testDeco(x):
    print(x)
    yield
    return x
testDeco(11)