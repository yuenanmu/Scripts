import requests

content =input("输入需要检索的内容：")
url=f"https://www.sogou.com/web?query={content}"#f-string格式化字符串，拼接URL

print("请求的URL:",url)

#headers,自爆家门
headers={
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0"
}
#发送GET请求,带上请求头
response=requests.get(url,headers=headers)
print("响应状态码:",response.status_code)
print("请求头信息:\n",response.request.headers)
print("响应内容:\n",response.text.encode('utf-8').decode('utf-8'))


"""
得到的响应内容是框架页面
内容需要Post请求才能得到
POST 请求，参数会放在 Body 里,不是直接进行url拼接
"""

