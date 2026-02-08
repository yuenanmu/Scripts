import re

# #findall()方法：返回一个列表，包含所有匹配结果
# result=re.findall(r"你好","你好你好你")
# print(result)

# result=re.findall(r"\d+","我有100r，今天又赚了14r")
# print(result)

# #迭代器
# result=re.finditer(r"\d+","我有100r，今天又赚了14r")
# for item in result:
#     print(item)           #返回一个match对象
#     print(item.group())   #match对象的方法，直接提取出数据

# #search()方法：返回一个match对象，找到第一个匹配结果就停止
# result=re.search(r"\d+","我有1r，今天又赚了14r")
# print("打印match对象:",result)
# print("对象的属性：",result.group())#match对象的方法，直接提取出数据

# #match()方法：查看开头是否匹配，是则返回一个match对象
# result=re.match(r"\d+","qq我有1r，今天又赚了14r")
# print("打印match对象：",result)
# #print("对象的属性：",result.group())#result为None，无法调用group()方法，否则会报错


# #预加载正则表达式：当需要多次使用同一个正则表达式时，可以预加载正则表达式，提高效率
# obj=re.compile(r"\d+")
# result=obj.findall("我有100r，今天又赚了14r")#不用每个都写一次正则表达式了
# reslult_1=re.findall(r"\d+","我有100r，今天又赚了14r")
# print("预加载正则表达式的结果：",result)
# print("未预加载正则表达式的结果：",reslult_1)



#模拟text文本中提取数据：1  使用()和2  ?P<name>来命名分组
S = "<div class='西游记'><span id='10010'>中国联通</span></div>" \
"<div class='西游记'><span id='10086'>中国移动</span></div>"

obj=re.compile(r"<span id='(?P<id>\d+)'>(?P<name>.*?)</span>")

result=obj.finditer(S)
i=0
for item in result:
    # print("id:",item.group("id"))
    # print("name:",item.group("name"))
    print(f"id_{i}: {item.group('id').ljust(5)} | name_{i} : {item.group('name').ljust(6)}")
    i+=1