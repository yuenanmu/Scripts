#优势：页面信息非对称时
from pyquery import PyQuery as pq
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
html="""
<ul>
    <li class="aaa"><a href="http://www.google.com">谷歌</a></li>
    <li class="aaa"><a href="http://www.baidu.com">百度</a></li>
    <li class="bbb"><a href="http://www.tengxun.com">腾讯</a></li>
    <li class="bbb"><a href="http://www.dingdong.com">京东</a></li>
    <li class="ccc"><a href="http://www.dongdongdong.com">咚咚咚</a></li>
</ul>
"""
#初始化PyQuery Object
doc=pq(html)#返回一个PyQuery对象:获取所有标签
# logging.debug(doc)
# print(type(doc))

# a=doc("a")#返回一个PyQuery对象:获取所有a标签
# logging.debug(a)
# print(type(a))

# #链式操作
# a=doc("li")("a")
# logging.debug(a)
# print(type(a))

a=doc(".aaa a")#类选择器，返回一个PyQuery对象:获取class为aaa的li标签下的所有a标签
# logging.debug(a)
# logging.debug(type(a))

#调用PyQuery对象的方法
for item in a.items():#items()方法将PyQuery对象转换为生成器，可以遍历每一个a标签
    href=item.attr("href")#获取a标签的href属性值
    name=item.text()
    html=item.html()#获取a标签内的HTML代码,标签+文本
    logging.debug(name+":"+href)
    logging.debug("html:"+html)

# 快速总结:
# 1. pyquery(选择器) 选择器选择的内容很多的时候. 需要一个一个处理的时候
# 2. items() 当选择器选择的内容很多的时候. 需要一个一个处理的时候
# 3. attr(属性名) 获取属性信息
# 4. text() 获取文本
# 5. html() 获取标签内的HTML代码,标签+文本


#修改
# doc(".aaa").after("""<div class="ccc">妈呀</div>""") # 插入HTML代码片段
# doc(".bbb").append("<span>我爱span</span>") # 向HTML内层标签中插入HTML片段
# doc(".aaa").html("<span>我是span</span>") # 修改标签内的html代码
# doc('.ccc').text("美滋滋") # 修改文本内容
doc(".ccc").attr("cs", "测试") # 添加属性(有则修改，无则添加：belike:字典)
doc(".ccc").remove_attr("cs") # 删除属性
logging.debug("修改数据之后的html:\n"+str(doc))
# print(doc)