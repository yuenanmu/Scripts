import requests
import asyncio
import aiofiles
import aiohttp
import json
import os
#https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}
async def aiodownload(cid,b_id,title):
    
    data={
        "book_id":b_id,
        "cid":f"{b_id}|{cid}",
        "need_bookinfo":1
    }
    #字典形式的data,使用json.dumps()转换成字符串形式的data
    url="https://dushu.baidu.com/api/pc/getChapterContent?data="+json.dumps(data)
    file_name=f"{title}.txt"
    file_path=os.path.join(target_folder,file_name)
    #创建文件夹
    os.makedirs(target_folder, exist_ok=True)  # exist_ok=True：文件夹已存在时不报错

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            json_data=await resp.json()#异步获取json数据
            content=json_data["data"]["novel"]["content"]
            async with aiofiles.open(file_path,mode="w",encoding="utf-8") as f:
                await f.write(content)#异步写入文件
    print(f"{title}下载完成")

async def getCatalog(url):
    resp=requests.get(url)
    if resp.status_code!=200:
        print(f"url:{url}请求失败")
        return  0
    json_data=resp.json()
    tasks=[]
    for item in json_data['data']["novel"]["items"]:
        title=item["title"]
        cid=item["cid"]
        print(f"小说标题：{title},cid:{cid}")
        task=asyncio.create_task(aiodownload(cid,b_id,title))
        tasks.append(task)
    await asyncio.wait(tasks)

if __name__ == "__main__":
    b_id="4306063500"
    url='https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'+b_id+'"}'
    target_folder="./novel_1"
    asyncio.run(getCatalog(url))