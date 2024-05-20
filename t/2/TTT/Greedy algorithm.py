# class Item:
#     def __init__(self,w:int,v:int):
#         self.w=w
#         self.v=v
#
# def fractional_knapsack(wgt: list[int], val: list[int], cap: int) -> int:
#         """分数背包：贪心"""
#         # 创建物品列表，包含两个属性：重量、价值
#         #这段代码的作用是根据给定的两个列表`wgt`和`val`，使用`zip()`函数将它们打包成元组，然后通过列表推导式生成一个新的`Item`对象列表`items`
#         items=[Item(w,v) for w,v in zip(wgt,val)]
#         # 按照单位价值 item.v / item.w 从高到低进行排序
#         items.sort(key=lambda item: item.v/item.w,reverse=True)
#         # 循环贪心选择
#         res=0
#         for item in items:
#             if item.w<cap:
#                 res+=item.v
#                 cap-=item.w
#             else:
#                 res+=(item.v/item.w)*cap
#                 break
#         return res
#
# if __name__ == '__main__':
#     wgt=[10,20,30,40,50]
#     val=[50,120,150,210,240]
#     cap=50
#     n=len(wgt)
#     res=fractional_knapsack(wgt,val,cap)
#     print(res)

def Max_capacity(ht:list[int])->int:
    #最大容量问题
    i,j=0,len(ht)-1
    res=0
    while i<=j:
        cap=min(ht[i],ht[j])*(j-1)
        res=max(cap,res)
        if ht[i]<ht[j]:
            i+=1
        else:
            j-=1
    return res

ht=[3,8,5,2,7,7,3,4]
res=Max_capacity(ht)
print(res)

import math
def max_product_cutting(n: int) -> int:
    #最大切分乘积问题
    if n<=3:
        return 1*(n-1)
    a,b=n//3,n%3
    if b==1:
        # 当余数为 1 时，将一对 1 * 3 转化为 2 * 2
        return int(math.pow(3, a - 1)) * 2 * 2
    if b==2:
        return int(math.pow(3,a))*2
    return int(math.pow(3,a))

n=58
res=max_product_cutting(n)
print(res)

"""
贪心算法通常用于解决最优化问题，其原理是在每个决策阶段都做出局部最优的决策，以期获得全局最优解。
"""