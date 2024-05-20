import random
def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]

def heapInsert(arr,index):
    while arr[index]>arr[(index-1)//2]:#当前节点数值大于父节点位置
        swap(arr,index,(index-1)//2)
        index=(index-1)//2

def heapify(arr,index,size):
    left=2*index+1
    while(left<size):
        largest=left+1 if left+1<size and arr[left+1]>arr[left] else left
        largest=largest if arr[largest]>arr[index] else index
        if (largest== index):
            break
        swap(arr,largest,index)
        index=largest
        left=2*index+1

def heapsort(arr):
    if arr is None  or len(arr)<2:
        return arr

    #将所有数字搞成大根堆1
    for i in range(len(arr)-1,-1,-1):
        heapify(arr,i,len(arr))
#在这里，n - 1 是起始值，-1 是终止值，-1 是步长，表示从n - 1递减到-1。这样的写法用于逆序迭代。
    #2 for i in range(len(arr)):
    #     heapInsert(arr,i)

    size=len(arr)

    swap(arr, 0 , size-1)

    while(size>0):
        heapify(arr,0,size  ) #0位置上的数重新调整位置
        swap(arr, 0, size - 1)#0位置上的数与heapsize最后一个数交换,heapsize减小
        size-=1
    return  arr

arr=[random.randint(0,10000) for i in range(10)]
print(arr)
print(heapsort(arr))
