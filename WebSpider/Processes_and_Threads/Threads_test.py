from threading import Thread
import time

def worker():
    start=time.time()
    for i in range(20):
        print("worker:",i)
    end=time.time()
    print("Worker thread time:", end - start)
def func(name):
    for i in range(20):
        print(name,i)
class MyThread(Thread):
    def run(self):
        start=time.time()
        for i in range(20):
            print("CWorker:",i)
        end=time.time()
        print("CWorker thread time:", end - start)

if __name__ == "__main__":
    main_start=time.time()
    worker_thread=Thread(target=worker)#创建线程对象，target参数指定线程要执行的函数
    worker_thread.start()#多线程可以开始执行的工作状态，不一定立马开始执行，取决于CPU调度
    cworker_thread=MyThread()#创建线程对象，调用run方法
    cworker_thread.start()
    func1_thread=Thread(target=func,args=("func1_thread",))#传递参数给线程函数，args参数是一个元组，要“，”
    func1_thread.start()
    func2_thread=Thread(target=func,args=("func2_thread",))#传递参数给线程函数，args参数是一个元组，要“，”
    func2_thread.start()
    #三个线程先并发执行，主线程继续执行下面的代码
    worker_thread.join()#等待worker_thread线程执行完毕
    cworker_thread.join()#等待cworker_thread线程执行完毕
    func1_thread.join()
    func2_thread.join()
    for i in range(20):
        print("main:",i)
    main_end=time.time()
    print("Main thread time:", main_end - main_start)