import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
def init_chrome_driver(driver_path):
    service=Service(executable_path=driver_path)
    driver=webdriver.Chrome(service=service)
    return driver

def operate_browser(browser,url):
    browser.get(url)
    time.sleep(2)
    windows = browser.window_handles  # 返回列表，按打开顺序排列
    # 2. 切换窗口
    browser.switch_to.window(windows[1])  # 切换到第二个标签页
    # 3. 新建标签页
    browser.execute_script("window.open('https://www.taobao.com')")  # JS新建标签
    # 4. 关闭当前标签并切回原标签
    browser.close()
    browser.switch_to.window(windows[0])

def close_browser(browser):
    input("任意键退出")
    browser.quit()
if __name__ == "__main__":
    driver_path=r"d:\git\scripts\WebSpider\Selenium\chromedriver.exe"
    browser=init_chrome_driver(driver_path)
    url="http://www.santostang.com/2018/07/04/hello-world/"
    operate_browser(browser,url)
    close_browser(browser)
