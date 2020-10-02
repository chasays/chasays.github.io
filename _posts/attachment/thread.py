from multiprocessing import Pool, Process
from os import name
from queue import LifoQueue
import os, time, random

def process_test(name):
    start = time.time()
    print(f'{name}, {os.getpid()}')
    time.sleep(random.random()*3)
    print(f'engding: {time.time()-start} sec')

if __name__=='__main__':
    ## 多进程
    pro = Process(target=process_test, args=('Thread_1',))
    pro.start()
    pro.join()

    ## 大量的子进程
    p = Pool() # default is CPU core number
    for i in range(5):
        p.apply_async(process_test, (f'Process_{i+1}',))
    p.close()
    p.join()
    print('ending')


