#爬取豆瓣电影Top250
#获取页面源代码
#正则提取数据
#保存文件
import re 
import requests
#设置调试开关
DEBUG_GET_HTML=0
DEBUG_EXTRACT_DATA=0
DEBUG_SAVE_DATA=1
def debug_get_html(*args,**kwargs):
    if DEBUG_GET_HTML:
        print('[DEBUG]-获取源代码',*args,**kwargs)
def debug_extract_data(*args,**kwargs):
    if DEBUG_EXTRACT_DATA:
        print('[DEBUG]-提取数据',*args,**kwargs)
def debug_save_data(*args,**kwargs):
    if DEBUG_SAVE_DATA:
        print('[DEBUG]-保存数据',*args,**kwargs)
url="https://movie.douban.com/top250"

headers={
    "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0"
}
print("正在获取页面源代码...")
resp=requests.get(url,headers=headers)
resp.encoding="utf-8"#这里不会乱码，不设置也可以
pageSource=resp.text
debug_get_html("打印获取的页面源代码：\n",pageSource)


#编写正则表达式(##########在信息的本行找匹配的内容，在信息的前后找匹配的内容#######)
pattern=r'<div class="item">.*?'\
        r'<span class="title">(?P<name>.*?)</span>.*?'\
        r'<div class="bd">.*?导演: (?P<director>.*?)&nbsp.*?</p>.*?'\
        r'<br>.*?(?P<year>.*?)&nbsp.*?'\
        r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'\
        r'<span>(?P<num>.*?)人评价</span>'
obj=re.compile(pattern,re.S)#预编译,利用py的re.S让.匹配换行符


#result=obj.findall(pageSource)#返回一个列表，列表中的每个元素都是一个元组，元组中包含了正则表达式中每个分组匹配到的内容
# print(result.group("name"))#这里会报错，因为findall方法返回的是一个列表，而不是一个match对象，所以无法调用group方法

csv_data=[]
csv_header='电影名,导演,上映时间,评分,评价人数\n'
csv_data.append(csv_header)#添加表头
#使用finditer方法，返回一个迭代器，迭代器中的每个元素都是一个match对象，可以调用group方法提取数据
result=obj.finditer(pageSource)
print("正在提取数据...")
for item in result:
    name=item.group("name").strip()
    director=item.group("director").ljust(10)
    year=item.group("year").strip().ljust(5)#去除字符串两端空格
    score=item.group("score").ljust(6)
    num=item.group("num").ljust(10)
    debug_extract_data(f"电影名称：{name} | 导演：{director} | 上映年份：{year} | 评分：{score} | 评价人数：{num}")
    csv_data.append(f"{name},{director},{year},{score},{num}\n")

#最后一次性写入所有数据
print("正在保存数据到Top250.csv文件中...")
with open("Top250.csv","w",encoding="utf-8") as f:#自动关闭文件，不需要再写f.close()了
    f.writelines(csv_data)
    debug_save_data("数据已保存到Top250.csv文件中！")
