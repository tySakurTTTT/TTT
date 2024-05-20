import random
def Insertion(list):
    n=len(list)
    for i in range(1,n):
        key=i-1
        mark=list[i]
        while key>=0 and list[key]>mark:
            list[key+1]=list[key]
            key-=1
        list[key+1]=mark
    return list


list=[random.randint(0,10000) for i in range(10)]
print(list)
print(Insertion(list))