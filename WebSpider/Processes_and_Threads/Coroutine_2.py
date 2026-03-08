import asyncio
import time

async def download(url):
    print("start downloading:",url)
    await asyncio.sleep(2)
    print("end downloading:",url)
    pass

async def main():
    start=time.time()
    urls=[
        "http://www.baidu.com",
        "http://www.bilibili.com",
        "http://www.zhihu.com"
    ]
    tasks=[]
    #使用asyncio.create_tasks创建任务对象，并将对象添加到列表中
    for url in urls:
        d=asyncio.create_task(download(url))
        tasks.append(d)
    await asyncio.wait(tasks)
    end=time.time()
    print(f"Main thread time:{end-start}")


if __name__ =="__main__":
    asyncio.run(main())