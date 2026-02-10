from lxml import etree


xml="""
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10010">周芷若</nick>
        <nick class="joy">周杰伦</nick>
        <nick class="jolin">蔡依林</nick>
        <div>
            <nick>惹了</nick>
        </div>
    </author>
    <partner>
        <nick id="ppc">胖胖陈</nick>
        <nick id="ppbc">胖胖不陈</nick>
    </partner>
</book>
"""

#创建etree对象
etree_obj=etree.XML(xml)
# result_list=etree_obj.xpath("/book")#返回一个列表,列表中的每个元素都是一个Element对象

#获取对象列表
# result_list=etree_obj.xpath("/book/nick")
#Elment对象的属性和方法
# print(result[0].tag)#获取标签名称：book
# print(result[0].text)#获取文本内容：\n    \n    \n
# print(result[0].get("id"))#获取属性内容：None


#直接获取数据
# result_list=etree_obj.xpath("/book/nick/text()")#返回一个列表，列表中的每个元素都是一个字符串
result_list=etree_obj.xpath("/book/*/nick/text()")#使用通配符*，匹配任意标签
result_list=etree_obj.xpath("/book/*/nick[@id='10086']/text()")#[]是属性筛选
result_list=etree_obj.xpath("/book/author/nick/@class")#获取属性内容
#操作列表
print(result_list)
print(result_list[0])#获取列表元素
