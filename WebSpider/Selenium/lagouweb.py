import selenium.webdriver as webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
def init_chrome_driver(driver_path):
    service=Service(executable_path=driver_path)
    driver=webdriver.Chrome(service=service)
    return driver

def init_chrome_driver2(driver_path):
    chrome_options = Options()
    # 1. 核心：隐藏webdriver特征
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    # 2. 禁用自动化提示条
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    # 3. 模拟真实窗口（不要用无头模式，手动操作需要可视化）
    chrome_options.add_argument("--start-maximized")
    # # 4. 加载浏览器本地配置（保留Cookie、历史记录，更像真人）
    #chrome_options.add_argument("--user-data-dir=C:\\Users\\PC\\AppData\\Local\\Google\\Chrome\\User Data")  # Windows路径
    # chrome_options.add_argument("--user-data-dir=/Users/你的用户名/Library/Application Support/Google/Chrome")  # Mac路径

    # 启动Driver
    driver = webdriver.Chrome(
        service=Service(executable_path=driver_path),#Service(ChromeDriverManager().install()),#Service(executable_path=driver_path),
        options=chrome_options
    )
    # 额外：执行JS彻底隐藏webdriver
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver
def slider_verify(browser):#,slider_xpath,track
    # wait = WebDriverWait(browser,10)
    # slider = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#nc_1_n1z")))
    browser.implicitly_wait(5)#不加这个会报错，因为页面元素还没有加载出来，找不到滑块元素
    slider=browser.find_element(By.ID,"nc_1_n1z")
    #模拟滑动滑块
    #点击
    action=ActionChains(browser)
    action.click_and_hold(slider).perform()
    time.sleep(random.uniform(0.3,0.5))
    #拖动
    taotal_distance=300
    action.move_by_offset(
        random.randint(95,105),
        random.randint(-3,3)
    ).perform()
    time.sleep(random.uniform(0.3,0.5))
    action.move_by_offset(
        random.randint(140,150),
        random.randint(-2,2)
    ).perform()
    time.sleep(random.uniform(0.3,0.5))
    action.move_by_offset(
        random.randint(45,55),
        random.randint(-2,2)
    ).perform()
    #松开
    action.release().perform()

def search_jobs(browser,keyword):
    #清除广告
    try:
        browser.implicitly_wait(5)
        script="var ad=document.querySelector('div[class*=\"loginBar\"]');" \
        " ad.parentNode.removeChild(ad);"
        browser.execute_script(script)
        print("广告已关闭")
    except:
        print("没有广告")
    #输入搜索关键词并点击搜索
    #等待
    time.sleep(2)#直接这个阻塞式等待就好！
    wait=WebDriverWait(browser,7)
    search_input=browser.find_element(By.ID,"search_input")
    search_input.clear()
    search_input.send_keys(keyword)
    search_btn=wait.until(EC.element_to_be_clickable((By.ID,"search_button")))
    search_btn.click()
    time.sleep(2)
    search_input.clear()
    time.sleep(1)
    search_input.send_keys("python")
    search_btn.click()
    time.sleep(1)
    browser.refresh()
    browser.back()
    browser.forward()
    # browser.quit()
    browser.close()

def operate_browser(browser,url):
    browser.get(url)
    slider_verify(browser)
    search_jobs(browser,"区块链")
    time.sleep(2)
    # windows = browser.window_handles  # 返回列表，按打开顺序排列
    # # 2. 切换窗口
    # browser.switch_to.window(windows[1])  # 切换到第二个标签页
    # # 3. 新建标签页
    # browser.execute_script("window.open('https://www.taobao.com')")  # JS新建标签
    # # 4. 关闭当前标签并切回原标签
    # browser.close()
    # browser.switch_to.window(windows[0])

def close_browser(browser):
    input("任意键退出")
    browser.quit()
if __name__ == "__main__":
    driver_path=r"d:\git\scripts\WebSpider\Selenium\chromedriver.exe"
    browser=init_chrome_driver2(driver_path)
    url="https://www.lagou.com/wn/"
    #"https://www.lagou.com/wn/zhaopin?kd=%E5%8C%BA%E5%9D%97%E9%93%BE&city=%E5%85%A8%E5%9B%BD"
    # #"http://www.santostang.com/2018/07/04/hello-world/"
    operate_browser(browser,url)
    close_browser(browser)
