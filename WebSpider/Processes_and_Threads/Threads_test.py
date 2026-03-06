from threading import Thread
import time

def worker():
    start=time.time()
    for i in range(200):
        print("worker:",i)
    end=time.time()
    print("Worker thread time:", end - start)

class MyThread(Thread):
    def run(self):
        start=time.time()
        for i in range(200):
            print("CWorker:",i)
        end=time.time()
        print("CWorker thread time:", end - start)

if __name__ == "__main__":
    main_start=time.time()
    worker_thread=Thread(target=worker)#创建线程对象，target参数指定线程要执行的函数
    worker_thread.start()#多线程可以开始执行的工作状态，不一定立马开始执行，取决于CPU调度
    
    cworker_thread=MyThread()#创建线程对象，调用run方法
    cworker_thread.start()
    for i in range(200):
        print("main:",i)
    main_end=time.time()
    print("Main thread time:", main_end - main_start)