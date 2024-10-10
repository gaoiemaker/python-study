# python 中实现多进程
# 在Unix/Linux下，可以使用fork()调用实现多进程。

# 要实现跨平台的多进程，可以使用multiprocessing模块。

# 进程间通信是通过Queue、Pipes等实现的。
from multiprocessing import Process, Pool
import os,time,random



# print("Process (%s) start...." % os.getpid())

# Only works on Unix/Linux/Mac:

# pid = os.fork()

# if pid == 0:
#     print("我是子线程%s,我的父线程是%s" % (os.getpid(), os.getppid()))
# else:
#     print("父线程%s，创建了一个子线程%s" % (os.getpid(), pid))


# 使用process启动线程


# def run_proc(name):
#     print("process运行了子线程%s(%s)" % (name, os.getpid()))


# if __name__ == "__main__":
#     print("父线程:%s", os.getpid())
#     p = Process(target=run_proc, args=("test",))
#     print("子线程启动了")
#     p.start()
#     p.join()
#     print('子线程结束')

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(4):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')