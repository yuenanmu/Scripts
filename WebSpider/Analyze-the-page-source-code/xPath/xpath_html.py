from lxml import etree

html="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>fltle</title>
</head>
<body>
    <ul>
        <li><a href="http://www.baidu.com">百度</a></li>
        <li><a href="http://www.google.com">谷歌</a></li>
        <li><a href="http://www.sogou.com">搜狗</a></li>
    </ul>
    <ol>
        <li><a href="feiji">飞机</a></li>
        <li><a href="huoche">火车</a></li>
        <li><a href="qiche">汽车</a></li>
    </ol>
    <div class="job">李嘉诚</div>
    <div class="common">胡辣汤</div>
</body>
</html>

"""
#创建etree对象
etree_obj=etree.HTML(html)

li_list=etree_obj.xpath("//li")#返回一个list

for li in li_list:
    a=li.xpath("./a")#./表示当前标签下的a标签,返回列表
    text=a[0].text
    href=a[0].get("href")
    print(text,href)