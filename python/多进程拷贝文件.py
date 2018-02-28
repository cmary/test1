import os
from multiprocessing import Pool, Manager, Queue


# 拷贝文件夹
def copy(name, old_name, new_name, queue):
    '''work for copy'''
    #print(name)
    fr = open(old_name + "/" + name)
    fw = open(new_name + "/" + name, "w")
    #print("--------------")
    content = fr.read()
    fw.write(content)
    fr.close()
    fw.close()
    queue.put(name)


def main():
    old_name = input("请输入文件文名字")
    new_name = old_name + "复件"
    # print(new_name)

    # 新建文件夹
    os.mkdir(new_name)

    # 获取文件夹中所有文件的名字
    files_names = os.listdir(old_name)
    # print(files)

    # 使用多进程的方式copy原来文件夹的所有文件到新文件夹中
    po = Pool(5)
    queue = Manager().Queue()
    for name in files_names:
        po.apply_async(copy, args=(name, old_name, new_name, queue))

    num = 0
    allnum = len(files_names)
    while True:
        queue.get()
        num += 1
        copyrate = num / allnum
        print("\r 进度是：%.2f%%" % (copyrate * 100), end="")
        if num == allnum:
            break
    print("拷贝完毕")


if __name__ == '__main__':
    main()