from bs4 import BeautifulSoup

html="""
    <ul>
        <li><a href="zhangwuji.com">张无忌</a></li>
        <li id="abc"><a href="zhouxingchi.com">周星驰</a></li>
        <li><a href="zhubajie.com">猪八戒</a></li>
        <li><a href="wuzetian.com">武则天</a></li>
    </ul>
"""
#创建BeautifulSoup对象
soup=BeautifulSoup(html,"html.parser")

soup.prettify()#格式化输出HTML代码
