from bs4 import BeautifulSoup
import logging
logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")

html="""
    <ul>
        <li><a href="zhangwuji.com">张无忌</a></li>
        <li id="abc"><a href="zhouxingchi.com">周星驰</a></li>
        <li><a href="zhubajie.com">猪八戒</a></li>
        <li><a href="wuzetian.com">武则天</a></li>
        <a href="sunwukong.com">孙悟空</a></li>
    </ul>
"""
#创建BeautifulSoup对象
soup=BeautifulSoup(html,"html.parser")

#logging.debug("GET_HTML:%s\n",soup.prettify())#格式化输出HTML代码,需要占位符
#print("GET_HTML_22222\n",soup.prettify())

li=soup.find("li",id="abc")#找特定标签,返回一个Tag对象
logging.debug(type(li))#<class 'bs4.element.Tag'>,返回一个Tag对象
a=li.find("a")
logging.debug(a.text)#获取文本内容：周星驰
logging.debug(a.get("href"))#获取属性内容：zhouxingchi.com

li_list=soup.find_all("li")#找多个标签，返回一个列表，列表中的每个元素都是一个Tag对象
logging.debug(type(li_list))
logging.debug(li_list)
for item in li_list:
    a=item.find("a")
    text=a.text
    href=a.get("href")
    logging.info("文本内容：%s,链接地址：%s",text,href)
