import random
def bubble(list):
    n=len(list)
    for i in range(n):
        flag=True#标记
        for j in range(1,n-i):  #每轮找到最大的数值
            if list[j-1]>list[j]:
                list[j-1],list[j]=list[j],list[j-1]
                flag=False
        if flag:# 某一趟遍历如果没有数据交换，则说明已经排好序了，因此不用再进行迭代了
                break
    return  list

list=[random.randint(0,10000) for i in range(10)]
print(list)
print(bubble(list))