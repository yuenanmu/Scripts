from multiprocessing import Process

def func():
    for i in range(20):
        print("子进程：",i)
class MyProcess(Process):
    def run(self):
        for i in range(20):
            print("MyProcess子进程：",i)
if __name__ == "__main__":
    func_process=Process(target=func)
    func_process.start()#启动子进程，调用func函数
    my_process=MyProcess()
    my_process.start()
    func_process.join()
    my_process.join()
    for i in range(500):
        print("主进程：",i)