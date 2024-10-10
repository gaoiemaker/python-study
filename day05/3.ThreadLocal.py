# 一个全局dict存放所有的数据，然后以thread自身作为key获得线程对应的数据 全局字典 就是 threadlocal、

import threading

local_school = threading.local()


def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread,args=('noble',),name='t1')
t2 = threading.Thread(target=process_thread,args=('jj',),name='t2')

t1.start()
t2.start()
t1.join()
t2.join()

## 一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。