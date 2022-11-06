import random
import os
import zipfile


def generator(chap, problem, test_num, file_py=None):
    address = f"./{chap}/{problem}"
    config_ini(test_num, address, file_py)
    zip_file(problem, address)


def config_ini(test_num, address, file_py):
    mark = score(100, test_num)
    if not os.path.exists(address):
        os.makedirs(address)
    with open(f"{address}/Config.ini", "w") as f:
        f.writelines(f"{test_num}\n")
        for k in range(test_num):
            f.writelines(f"input{k}.txt|output{k}.txt|1|{mark[k]}\n")
    for i in range(test_num):
        with open(f"./{address}/input{i}.txt", "w") as input_txt:
            input_txt.write(input_str := input(f"In[{i}]@"))
        if file_py is not None:
            pass
        else:
            with open(f"./{address}/output{i}.txt", "w") as output_txt:
                output_txt.write(input(f"Out[{i}]@"))

def score(amount, num):
    list1 = []
    for i in range(0,num-1):
        a = random.randint(0,amount)    # 生成 n-1 个随机节点
        list1.append(a)
    list1.sort()                        # 节点排序
    list1.append(amount)                # 设置第 n 个节点为amount，即总金额

    list2 = []
    for i in range(len(list1)):
        if i == 0:
            b = list1[i]                # 第一段长度为第 1 个节点 - 0
        else:
            b = list1[i] - list1[i-1]   # 其余段为第 n 个节点 - 第 n-1 个节点
        list2.append(b)

    return list2

def zip_file(problem, address):
    os.chdir(address)
    with zipfile.ZipFile(f"{problem}.zip", mode="w") as archive:
        for file_list in os.listdir():
            if file_list == f"{problem}.zip":
                continue
            archive.write(file_list)
    os.chdir(os.path.dirname(__file__))

chap = input("Chap@")
problem = input("Problem@")
test_num = int(input("test_num@"))
generator(chap, problem, test_num)