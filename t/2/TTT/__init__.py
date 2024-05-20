# result=0
# for i in range(12345678,98765433):
#     if str(2023) not in str(i):
#         result+=1
# print(result)
#
#
#
# import re
# result = re.compile(r"\d*".join("2023"))
# nums=range(12345678,98765433)
# print(sum(not re.search(result, i) for i in map(str, nums)))
#
# count = 0
# for i in range(12345678, 98765433):
#         flag = True
#         for digit in str(i):
#             if digit == '2':
#                 if str(i).find('2', str(i).find('2')+1) == -1:
#                         flag = False
#                         break
#                 elif digit == '0' or digit == '3':
#                         flag = False
#                         break
#
# if flag:
#     count += 1
#
# print(count)
#
import math

# s=[0]+list(input())
# for i in range(1,len(s)):
#     s[i]=ord(s[i])-96
#
# dp=[0]*(len(s)+1)
# dp[1]=s[1]
# for i in range(2,len(s)):
#     dp[i]=max(dp[i-1],dp[i-2]+s[i])
#
# print(dp[len(s)-1])

# def find2023(nums):
#     s=str(nums)
#     first=s.find("2")
#     if first==-1:
#         return False
#     sec=s.find("0",first+1)
#     if sec==-1:
#         return False
#     thd=s.find("2",sec+1)
#     if thd==-1:
#         return False
#     fth=s.find("3",thd+1)
#     if fth==-1:
#         return False
#     return True
#
# result=0
# for i in range(12345678,98765433):
#     res=find2023(i)
#     if not res :
#         result+=1
# print(result)


# n=int(input())
# x=[0]+list(map(int,list(input())))[::-1]
# y=[0]+list(map(int,list(input())))[::-1]
# print(x)
# print(y)
# dp=[[0]*3 for i in range(n+1)]
# dp[1][0]=abs(x[1]-y[1])
# dp[1][1]=10-x[1]+y[1]
# dp[1][2]=10+x[1]-y[1]
# print(dp[1][0])
# print(dp[1][1])
# print(dp[1][2])
# for i in range(2,n+1):
#     dp[i][0] = min(dp[i - 1][0] + abs(x[i] - y[i]), dp[i - 1][1] + abs(x[i] - y[i] + 1),
#                    dp[i - 1][2] + abs(x[i] - y[i] - 1))
#     dp[i][1] = min(dp[i - 1][0] + 10 - x[i] + y[i], dp[i - 1][1] + 10 - (x[i] + 1) + y[i],
#                    dp[i - 1][2] + 10 - (x[i] - 1) + y[i])
#     dp[i][2] = min(dp[i - 1][0] + 10 - y[i] + x[i], dp[i - 1][1] + 10 - y[i] + (x[i] + 1),
#                    dp[i - 1][2] + 10 - y[i] + (x[i] - 1))
# print(min(dp[n][0], dp[n][1], dp[n][2]))

# ans=0
# for r in range(1012,2023):
#     tar=r*2+1
#     l=tar-2023
#     tmp=(l+r)*(r-l+1)//2
#     if tmp<ans:
#         break
#     ans=tmp
#     print(l,r,tmp)
# print(ans)

#
# n=list(input())
# print("".join(sorted(n)))
#
# n=input()
# print("".join(sorted(n)))


# x=int(input()[1])
# size=[(1189,841)]
#
# for i in range(x):
#     last_a,last_b=size[-1]
#     size.append((last_b,last_a//2))
# print(size[x])

# n=int(input())
# m=int(input())
# s=list(range(1,n+1))
# s.sort(key=lambda x:sum(int (i) for i in str(x)))
# print(s[m-1])
#
# N=10000
# n=int(input())
# a=[int(input()) for _ in range(n)]
#
# dp=[0 for _ in range(N)]
# g=a[0]
# for i in range(n):
#     g=math.gcd(g,a[i])
# if g==1:
#     dp[0]=1
#     for i in range(n):
#         for j in range(a[i],N):
#             dp[j]=max(dp[j],dp[j-a[i]])
#
# print(N-sum(dp))

#
# N,K=map(int,input().split())
# a=(int(input()) for i in range(N))
# cnt=0
# dp=[0 for i in range(N)]
# dp[0]=1
# for i in range(1,N+1):
#     if dp[i]-dp[i+1]==K:
#         cnt+=1
# print(cnt)

ans=0
for i in range(1,2021):
    if str(2)  in str(i):
        ans += 1
print(ans)
#
# s=''
# for i in range(1,2021):
#     s+=str(i)
# print(s)
#

from datetime import *
dt1=datetime(1901,1,1)
dt2=datetime(2000,12,31)
dt=dt2-dt1
print(dt)
print(dt/7)

date="2020 4019 1285 "

s=1
num=date.split()
for i in num:
    s=s*int(i)
cnt=0
while s%10==0:
    s//=10
    cnt+=1
print(cnt)

sum=0
for i in range(1,2020):
    s=str(i)
    if "2" in s or "0" in s or "1" in s or "9" in s :
        sum+=i*i
print(sum)


def searchInsert(nums: list[int], target: int) -> int:
    left,right=0,len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]<target:
            left=mid+1
        if nums[mid]>target:
            #else:
            right=mid-1
    return left


nums=[1,3,5,6]
target=2
s=searchInsert(nums,target)
print(s)