import requests
import json

# 1. 配置请求标头（完全匹配你提供的标头）
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "www.xinfadi.com.cn",
    "Origin": "http://www.xinfadi.com.cn",
    "Referer": "http://www.xinfadi.com.cn/priceDetail.html",
    "X-Requested-With": "XMLHttpRequest"
}

url = "http://www.xinfadi.com.cn/getPriceData.html"

# 3. 构造请求参数（表单格式，可根据需要调整参数）
data = {
    "limit": "20",    # 每页返回20条数据
    "current": "1",   # 第1页
    "pubDateStartTime": "",  # 开始日期（可选）
    "pubDateEndTime": "",    # 结束日期（可选）
    "prodPcatid": "",        # 产品大类（可选）
    "prodCatid": "",         # 产品小类（可选）
    "prodName": ""           # 产品名称（可选，如"白菜"）
}

def crawl_xinfadi():
    try:
        # 发送POST请求（匹配标头中的POST方法）
        response = requests.post(
            url=url,
            headers=headers,
            data=data,
            timeout=10,  # 超时时间，避免卡死
            verify=False  # 忽略HTTPS证书（若有）
        )
        print(response.url)
        # 检查请求是否成功
        print(response.raise_for_status())
        
        # 解析JSON数据（标头返回Content-Type是application/json）
        result = response.json()
        print("爬取成功！数据示例：")
        # 打印前3条数据，方便查看
        for item in result.get("list", [])[:3]:
            print(f"产品：{item.get('prodName')}，价格：{item.get('avgPrice')}元/{item.get('unitInfo')}")
        
        # 保存数据到本地JSON文件
        with open("xinfadi_price.json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
        print("数据已保存到 xinfadi_price.json")
        
    except requests.exceptions.RequestException as e:
        print(f"爬取失败：{e}")
    except json.JSONDecodeError:
        print("解析失败：返回的不是JSON格式")
    except Exception as e:
        print(f"未知错误：{e}")

if __name__ == "__main__":

    crawl_xinfadi()