import selenium.webdriver as webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from chaojiying  import Chaojiying_Client
def init_chrome_driver(executable_path):
    #配置service和option
    option=Options()
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_experimental_option('useAutomationExtension', False)
    option.add_argument("--disable-blink-features=AutomationControlled")
    option.add_argument("--start-maximized")
    service=Service(executable_path=executable_path)
    driver=webdriver.Chrome(service=service)
    #js隐藏webdriver特征
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver
def chaojiying_verify(browser,wait):
    try:
        #截图验证码
        pic_element=wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div[3]/div[1]/form/div/img")))
        pic_npg=pic_element.screenshot_as_png#将验证码图片以二进制的形式返回!!
        #调用超级鹰接口识别验证码
        chaojiying=Chaojiying_Client('18779046135', 'lg9gs52m', '978616')	#用户中心>>软件ID 生成一个替换 96001
        result=chaojiying.PostPic(pic_npg,1902)
        if result:#有效性验证
            v_code=result['pic_str']
            print("识别成功，返回结果：",result)
        else:
            print("识别失败，返回结果：",result)
            v_code=""
    except Exception as e:
        print("识别失败：",e)
        v_code=""
    
    return v_code
def sleep(inum):
    time.sleep(random.uniform(1,1+inum))
def log_in(browser,wait,username,password):
    url="https://www.chaojiying.com/user/login/"
    sleep(1)
    browser.get(url)
    #输入用户名以及密码
    username_input=wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input")))
    password_input=wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input")))
    sleep(0.5)
    username_input.send_keys(username)
    password_input.send_keys(password)
    #验证码
    v_code=chaojiying_verify(browser,wait)                           
    v_code_input=wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input")))
    v_code_input.send_keys(v_code)
    #点击登录按钮
    log_in_btn=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input")))
    log_in_btn.click()

def browser_close(browser):
    input("按任意键退出")
    browser.quit()

def main():
    driver_path=r"d:\git\scripts\WebSpider\Selenium\chromedriver.exe"
    browser=init_chrome_driver(driver_path)
    wait=WebDriverWait(browser,10)
    log_in(browser,wait,"18779046135","lg9gs52m")
    browser_close(browser)


if __name__ == '__main__':
    main()