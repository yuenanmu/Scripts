from selenium import webdriver 
from selenium.webdriver.chrome.service import Service

driver_path=r"d:\git\scripts\WebSpider\Selenium\chromedriver.exe"#不同电脑需要改文件名！
service=Service(executable_path=driver_path)#创建Service对象，指定chromedriver.exe的路径


Web=webdriver.Chrome(service=service)#初始化Chrome浏览器实例
#Web=Chrome(executable_path="./chromedriver.exe")#旧版本初始化直接指定路径
url="https://www.baidu.com/"

Web.get(url)
print(Web.title )


input("任意键退出")
Web.quit()
print("退出成功")