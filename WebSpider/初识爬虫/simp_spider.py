from urllib.request import urlopen

url="https://www.baidu.com"

resp=urlopen(url)  #返回的是一个 具有属性和方法的特殊对象

# #打印对象（显示所在地址信息）
# print(resp)
# #获取状态码
# print(resp.status)
# #获取响应头
# print("Content-Type:",resp.headers["Content-Type"])
# #获取网页内容
data=resp.read()           #byte类型，字节流
text=data.decode("utf-8")  #解码,str类型，字符串
#print(text)
with open("mybaidu.html",mode="w",encoding="utf-8") as f:
    f.write(text)#将内容写入到本地文件