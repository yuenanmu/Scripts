import requests
#POST 请求，参数会放在 Body 里,不是直接进行url拼接
url="https://fanyi.baidu.com/sug"

data={
    "kw":input("检索的内容：")
}

headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0"

}

resp=requests.post(url,data=data,headers=headers)
print("请求状态码：",resp.status_code)
print("响应内容：\n",resp.json())#返回字典
print("响应内容：\n",resp.text)#返回文本字符串,看不懂思密达~