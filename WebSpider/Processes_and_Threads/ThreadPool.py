from concurrent.futures import ThreadPoolExecutor

def task(name):
    for i in range(5):
        print(name,i)
if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=30) as t: #招募30个工人（线程）
        for i in range(40):    # 创建40个任务
            t.submit(task,name=f"Task{i}:\n")
    # 线程池会自动等待所有线程完成后再退出
    print("All tasks completed.")   