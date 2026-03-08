import asyncio 
import time
#定义协程函数，每个协程函数返回一个协程对象！
async def func1():
    print("func1 start")
    #time.sleep(1)
    await asyncio.sleep(1)#模拟IO操作，协程在等待期间可以让出控制权，其他协程可以继续执行
    print("func1 end")

async def func2():
    print("func2 start")
    await asyncio.sleep(2)
    print("func2 end")
async def func3():
    print("func3 start")
    await asyncio.sleep(3)
    print("func3 end")
async def main():
    start=time.time()
    #存储协程对象的列表
    task1=asyncio.create_task(func1())
    task2=asyncio.create_task(func2())
    task3=asyncio.create_task(func3())
    tasks=[task2,task3,task1]#创建任务对象列表
    # tasks=[func1(),func2(),func3()]#不允许直接创建协程对象列表了！
    await asyncio.wait(tasks)#等待所有协程执行完毕
    end=time.time()
    print(f"Main thread time:{end-start}")

if __name__ == "__main__":
    asyncio.run(main())