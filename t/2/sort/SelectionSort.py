import random
def Selection(list):
    n=len(list)
    for i in range(0,n):
        min=i
        for j in range(i+1,n):#每轮找到最大数值
            if list[j]<list[min]:
                min=j
        if min != i:
                list[i],list[min]=list[min],list[i]
    return list

list=[random.randint(0,10000) for i in range(10)]
print(list)
print(Selection(list))

