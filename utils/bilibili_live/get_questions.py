import time
with open(f"./bilibili/danmu/danmu_{time.strftime('%Y-%m-%d', time.localtime())}.md", "r", encoding="utf-8") as danmu_file:
    content = danmu_file.readlines()

with open(f"./bilibili/questions_{time.strftime('%Y-%m-%d', time.localtime())}.md", "w", encoding="utf-8") as q_file:
    idx = 1
    for item in content:
        if item.startswith("- [X]"):
            q_file.write(f"{idx}. - [ ] {item.split(' => ')[0][5:]}\n")
            idx += 1
    print("问题列表生成完毕！")