import random

arr:list[int]=[0]*5
nums:list[int]=[1,3,2,5,4]
print(arr,nums)

def Random_access(nums:list[int])->int:
    random_index=random.randint(0,len(nums)-1)
    random_num=nums[random_index]
    return random_num

print(nums)
print(Random_access(nums))

def insert(nums:list[int],index:int,num:int)->int:
    for i in range(len(nums)-1,index,-1):
        nums[i]=nums[i-1]
    nums[index]=num
print(nums)
print(insert(nums, 3, 6))

#遍历数组
def traverse(nums:list[int]):
    count=0
    #通过索引
    for i in range(len(nums)):
        count+=nums[i]
    #直接遍历数组元素
    for num in nums:
        count+=num
    # 同时遍历数据索引和元素
    for i,num in enumerate(nums):
        count+=nums[i]
        count+=num


count=0
arr2:list[int]=[1,223,56,36,56]
for i, num in enumerate(arr2):#对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），
                              # enumerate将其组成一个索引序列，利用它可以同时获得索引和值
    count += arr2[i]
    count += num
print(count)
print(count[i])