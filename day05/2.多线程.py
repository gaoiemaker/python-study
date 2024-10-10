import time, threading

# 新线程执行的代码:
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)

# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(10000000):
        # 需要锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 解锁
            lock.release()


t1 = threading.Thread(target=run_thread, args=(1,))
t2 = threading.Thread(target=run_thread, args=(2,))
# t3 = threading.Thread(target=run_thread, args=(3,))
# t4 = threading.Thread(target=run_thread, args=(4,))
t1.start()
t2.start()
t1.join()
t2.join()

print(balance)


# 多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。

# Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。
