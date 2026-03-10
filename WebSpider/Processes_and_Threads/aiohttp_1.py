import aiohttp
import asyncio

urls = [
    "https://picsum.photos/800/600.jpg",
    "https://picsum.photos/400/300.jpg",
    "https://picsum.photos/200/150.jpg"
]

async def aiodownload(url):
    name=url.rsplit("/",1)[1]#??
    #with语句自动close资源
    async with aiohttp.ClientSession() as session:#创建会话对象
        async with session.get(url) as resp:
            print(f"url: {url}, status: {resp.status}")
            with open(name,mode="wb") as f:
                f.write(await resp.content.read())#await挂起当前协程，等待结果返回
    print(f"{name}下载完成")

async def main():
    task=[]
    for url in urls:
        atask=asyncio.create_task(aiodownload(url))
        task.append(atask)#添加任务列表
    await asyncio.wait(task)

if __name__ == "__main__":
    asyncio.run(main())