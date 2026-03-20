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

#智能切换窗口，包括：窗口等待加载、窗口数量检查，窗口切换、窗口标题验证等
def switch_to_new_window(browser,wait,original_handles=None):
    """
    :param original_handles: 点击前的窗口句柄列表（不传则自动获取）
    """
    #等待新窗口加载
    try:
        if original_handles is None:
            original_handles = browser.window_handles[:]
        wait.until(EC.new_window_is_opened(original_handles))
        new_handles = [h for h in browser.window_handles if h not in original_handles]
        target_handle = new_handles[-1] if new_handles else browser.window_handles[-1]
        browser.switch_to.window(target_handle)
        print(f"切换到新窗口，标题: {browser.title}")
        return True
    except Exception as e:
        print(f"新窗口加载失败: {e}")
        return False
def switch_to_old_window(browser,wait,original_count=None):
    """
    :param original_count: 点击前的标签页数量（不传则自动获取）
    """
    #等待旧窗口加载
    try:
        if original_count is None:
            original_count = len(browser.window_handles)
        wait.until(lambda d:len(d.window_handles)<original_count)
        if len(browser.window_handles) >= 2:  # 先判断至少有2个窗口，避免索引越界
            old_window_handle=browser.window_handles[-2]
            browser.switch_to.window(old_window_handle)
            print(f"切换回旧窗口，标题: {browser.title}")
        else:
            print("只有唯一窗口，无法切换回旧窗口")
    except Exception as e:
        print(f"旧窗口切换失败: {e}")

def search_jobs(browser,keyword):
    #清除广告
    try:#执行js脚本删除广告元素，避免干扰后续操作
        script="var ad=document.querySelector('div[class*=\"loginBar\"]');" \
        " ad.parentNode.removeChild(ad);"
        browser.execute_script(script)
        print("广告已关闭")
    except Exception:
        print("没有广告")
    #输入搜索关键词并点击搜索
    #等待
    time.sleep(2)#直接这个阻塞式等待就好！
    wait=WebDriverWait(browser,7)
    search_input=browser.find_element(By.ID,"search_input")
    search_input.clear()
    search_input.send_keys(keyword)
    search_btn=wait.until(EC.element_to_be_clickable((By.ID,"search_button")))
    before_search_handles = browser.window_handles[:]
    search_btn.click()
    #点击搜索后会打开新窗口，切换到新窗口
    if not switch_to_new_window(browser,wait,before_search_handles):
        return
    
    jobs_window_handle = browser.current_window_handle#/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div[1]/div[1]|||/div[1]/div[1]/span/div/div[1]/a
    # 先滚动页面加载所有职位（避免动态加载漏项）
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)
    jobs_list=wait.until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div[1]/div')))
    if not jobs_list:#检查职位列表有效性
        print("没有找到职位列表")
        return
    else:
        print(f"找到{len(jobs_list)}个职位")
        print(f"职位列表元素: {jobs_list}")
        index=0
        for job in jobs_list:
            index+=1
            print(f"正在处理第{index}个职位")
            try:
                #首先：不一定找得到！！不用这个会报错，导致整个程序死掉
                #其次，一定要直接复制，别手写！！！
                position = wait.until(EC.presence_of_element_located((By.XPATH,'.//div[1]/div[1]/div[1]/a')))
                position_text=position.text
                print(f"职位: {position_text}")
                before_position_handles = browser.window_handles[:]
                position.click()#点击职位，打开新窗口
                time.sleep(random.uniform(1, 2))#模拟点击后的停留时间
                if not switch_to_new_window(browser,wait,before_position_handles):
                    continue
                try:
                    position_details=wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="job_detail"]/dd[2]/div[1]')))#职位详情元素
                    time.sleep(random.uniform(2, 4))
                    if not position_details:
                        print("没有找到职位详情")
                    else:
                        print(f"职位详情: ::::::::::::::::::::")
                except Exception as e:
                    print(f"职位详情元素不存在，跳过: {e}")
                finally:
                    time.sleep(random.uniform(2, 4))#模拟浏览职位的停留时间,sleep参数可以是小数
                    browser.close()
                    browser.switch_to.window(jobs_window_handle)
            except Exception as e:
                print(f"openWinPosition元素不存在，跳过: {e}")
            


    # search_input.clear()
    # time.sleep(1)
    # search_input.send_keys("python")#？会不会是没有切换窗口，导致clear失效？
    # search_btn.click()
    # time.sleep(1)
    # browser.refresh()
    # browser.back()
    # browser.forward()
    # # browser.quit()
    # browser.close()

def operate_browser(browser,url):
    browser.get(url)
    slider_verify(browser)
    search_jobs(browser,"区块链")
    time.sleep(2)


def close_browser(browser):
    # input("任意键退出")
    print("完成任务，正在关闭浏览器...")
    browser.quit()
if __name__ == "__main__":
    driver_path=r"d:\git\scripts\WebSpider\Selenium\chromedriver.exe"
    browser=init_chrome_driver2(driver_path)
    url="https://www.lagou.com/wn/"
    #"https://www.lagou.com/wn/zhaopin?kd=%E5%8C%BA%E5%9D%97%E9%93%BE&city=%E5%85%A8%E5%9B%BD"
    # #"http://www.santostang.com/2018/07/04/hello-world/"
    operate_browser(browser,url)
    close_browser(browser)
