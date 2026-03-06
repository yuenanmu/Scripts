from concurrent.futures import ProcessPoolExecutor

def task(name):
    for i in range(5):
        print(name,i)
if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=30) as p: #招募30个工人（进程）
        for i in range(40):    # 创建40个任务
            p.submit(task,name=f"Task{i}:\n")
    # 进程池会自动等待所有进程完成后再退出
    print("All tasks completed.")   