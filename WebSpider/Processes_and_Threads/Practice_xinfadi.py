import requests
import json
from multiprocessing import Pool,Manager
import time

URL="http://www.xinfadi.com.cn/getPriceData.html"
HEADERS={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0",
    "x-requested-with":"XMLHttpRequest",
    "host":"www.xinfadi.com.cn",
    "origin":"http://www.xinfadi.com.cn",
    "referer":"http://www.xinfadi.com.cn/priceDetail.html",
}
DATA={
    "limit":"20",
    "current":"1",
}
def crawl_one_page(page_num,result_list):
    """
    爬取一页并提取核心字段
    result_list：进程间共享的列表，用于储存结果
    """
    try:
        #发送Post请求
        resp=requests.post(
            url=URL,
            headers=HEADERS,
            data=DATA,
            timeout=10,
        )
        #状态码检验
        if resp.status_code!=200:
            print(f"第{page_num}页请求失败，状态码：{resp.status_code}")
        #数据解析
        json_data=resp.json()
        #print(f"第{page_num}页数据：{json_data}")
        #print(type(json_data))  #json_data是一个字典
        #提取核心字段
        products_list=json_data.get("list",[])#如果没用list字段，返回空列表[]
        if not products_list:
            print(f"第{page_num}页没有数据")
            return
        for product in products_list:
            item={
                "name":product.get("prodName","N/A"),
                "Cat":product.get("prodCat","N/A"),
                "avgprice":product.get("avgPrice","N/A"),
                "low_price":product.get("lowPrice","N/A"),
                "high_price":product.get("highPrice","N/A"),
                "date":product.get("pubDate","N/A"),
            }
            result_list.append(item)
        print(f"第{page_num}页提取完成，当前结果列表长度：{len(result_list)}")
        time.sleep(1.2) #适当休眠，避免过快请求
    except Exception as e:
        print(f"第{page_num}页请求异常：{e}")
        


if __name__ == '__main__':
    start_time=time.time()
    start_page=1
    end_page=10
    #创建Manager对象，用于进程间共享数据
    manager=Manager()
    result_list=manager.list()#创建一个共享列表
    #创建进程池
    pool=Pool(processes=4)
    with pool as p:
        #使用starmap分配任务，传递页码和共享列表
        pool.starmap(crawl_one_page,[(page_num,result_list) for page_num in range(start_page,end_page+1)])
    #保存结果到JSON文件
    with open("xinfadi_data.json","w",encoding="utf-8") as f:
        #将共享列表转换为普通列表后保存
        json.dump(list(result_list),f,ensure_ascii=False,indent=2)
    end_time=time.time()
    print(f"爬取完成，耗时{end_time-start_time:.2f}秒，结果保存到xinfadi_data.json")