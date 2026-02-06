#多参数的get请求：https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start=0&limit=20
import requests

url="https://movie.douban.com/j/chart/top_list"

data={
    "type":"13",
    "interval_id":"100:90",
    "action":"",
    "start":"0",
    "limit":"20"
}

headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0"
}

resp=requests.get(url,params=data,headers=headers)

print("url:",resp.url)
print("请求状态码：",resp.status_code)
print("响应内容：\n",resp.json())
