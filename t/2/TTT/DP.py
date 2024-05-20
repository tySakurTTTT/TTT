from math import inf, comb


class ListNode:
    def __init__(self,value=0,next=None):
        this.value=value
        this.next=next

class Solution:
    def backTrack(self,choices:list[int],state:int,res:list[int],n:int)->int:
        if state==n:
            res[0]=+1
        for choice in choices:
            if state+choice>n:
                continue
            backTrack(choices,state+choices,n,res)

    def climbing_stairs_backtrack(n: int) -> int:
        choices=[1,2]
        state=0
        res=[0]
        backTrack(choices,state,res,n)
        return res[0]

    def dfs(self,i:int)->int:
        if i==n or i==2:
            return i
        count=dfs(i-1)+dfs(i-2)
        return count

    def climbing_stairs_dfs(self,n:int)->int:
        return dfs(n)

    def dfs(self,i:int,mem:list[int])->int:
        if i==1 or i==2:
            return i
        if mem[i]!=-1:
            return mem[i]
        count=dfs(i-1,mem)+dfs(i-2,mem)
        mem[i]=count
        return count

    def climbing_stairs_dfsmem(self,n:int)->int:
        mem=[-1]*(n+1)
        return dfs(n,mem)

    def climbing_stairs_dp(self,n:int)->int:
        if n==1 or n==2:
            return n
        dp=[0]*(n+1)
        dp[1],dp[2]=1,2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]

    def min_cost_climbing_stairs_dp(self, cost:list[int]) -> int:
        n=len(cost)-1
        if n==1 or n==2:
            return cost[n]
        dp=[0]*(n+1)
        dp[1],dp[2]=1,2
        for i in range(3,n+1):
            dp[i]=min(dp[i-1],dp[i-2])+cost[i]
        return dp[n]

    def climbing_stairs_constraint_dp(n: int) -> int:
        if n==1 or n==2:
            return 1
        dp=[[0]*3 for _ in range(n+1)]
        dp[1][1],dp[1][2]=1,0
        dp[2][1],dp[2][2]=0,1
        for i in range(3,n+1):
            dp[i][1]=dp[i-1][2]
            dp[i][2]=dp[i-1][1]+dp[i-2][2]
        return dp[n][1]+dp[n][2]

    def min_path_sum_dfs(self,grid: list[list[int]], i: int, j: int) -> int:
        if i==0 and j==0:
            return grid[0][0]

        if i<0 or j<0:
            return inf
        up=self.min_path_sum_dfs(grid,i-1,j)
        left=self.min_path_sum_dfs(grid,i,j-1)
        return min(up,left)+grid[i][j]

    def min_path_sum_dfs_mem(
            self,grid: list[list[int]], mem: list[list[int]], i: int, j: int
    ) -> int:
        if i == 0 and j == 0:
            return grid[0][0]
        if i < 0 or j < 0:
            return inf
        # 若已有记录，则直接返回
        if mem[i][j] != -1:
            return mem[i][j]
        up = self.min_path_sum_dfs_mem(grid, mem, i-1, j)
        left = self.min_path_sum_dfs_mem(grid, mem, i, j-1)
        mem[i][j] = min(left,up) + grid[i][j]
        return mem[i][j]

    def min_path_sum_dp(slef,grid: list[list[int]]) -> int:
        n,m=len(grid),len(grid[0])
        dp=[[0]*m for _ in range(n)]#list * int 意思是将数组重复 int 次并依次连接形成一个新数组,
        # for _in range(n)仅将循环运行n次，等效于for i in range(n)，只不过_在后面不会用到，只是占位符

        dp[0][0]=grid[0][0]
        for j in range(1,m):
            dp[0][j]=dp[0][j-1]+grid[0][j]
        for i in range(1,n):
            dp[i][0]=dp[i-1][0]+grid[i][0]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[n-1][m-1]

    def knapsack_dfs(self,wgt:list[list[int]],val:list[list[int]],n:int,c:int):
        if n==0 or c==0:
            return 0
        if wgt[n-1]>c:
            return self.knapsack_dfs(wgt,val,n-1,c)
        # 计算不放入和放入物品 i 的最大价值
        no=self.knapsack_dfs(wgt,val,n-1,c)
        yes=self.knapsack_dfs(wgt,val,n-1,c-wgt[n-1])+val[n-1]
        return max(no,yes)

    def knapsack_dfs_mem(
            self,wgt: list[int], val: list[int], mem: list[list[int]], i: int, c: int
    ) -> int:
        if i==0 or c==0:
            return 0
        if wgt[i-1]>c:
            return self.knapsack_dfs_mem(wgt,val,mem,i-1,c)
        if mem[i-1][c]!=-1:
            return mem
        no=self.knapsack_dfs_mem(wgt,val,mem,i-1,c)
        yes=self.knapsack_dfs_mem(wgt,val[i-1],mem,i-1,c-wgt[i-1])+val[i-1]
        mem[i-1][c]=max(no,yes)
        return mem[i-1][c]

    def knapsack_dp(self,wgt: list[int], val: list[int], cap: int) -> int:
        n=len(wgt)
        dp=[[0]*(cap+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for c in range(1,cap+1):
                if wgt[i-1]>c:
                    dp[i][c]=dp[i-1][c]
                else:
                    dp[i][c]=max(dp[i-1][c],dp[i-1][c-wgt[i-1]]+val[i-1])
        return dp[n][cap]

    def unbounded_knapsack_dp(self,wgt: list[int], val: list[int], cap: int) -> int:
        n=len(wgt)
        dp=[[n]*(cap+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for c in range(1,cap+1):
                if wgt[i-1]>c:
                    dp[i][c]=dp[i-1][c]
                else:
                    dp[i][c]=max(dp[i-1][c],dp[i][c-wgt[i-1]]+val[i-1])
        return dp[n][cap]

    def coin_change_dp(self,coins: list[int], amt: int) -> int:
        n=len(coins)
        dp=[[0]*(amt+1) for _ in range(n+1)]
        Max=amt+1
        for a in range(1,amt+1):
            dp[0][a]=Max
        for i in range(1,n+1):
            for a in range(1,amt+1):
                if coins[i-1]>a:
                    dp[i][a]=dp[i-1][a]
                else:
                    dp[i][a]=min(dp[i-1][a],dp[i][a-coins[i-1]]+1)
        return dp[n][amt] if dp[n][amt] != Max else -1

    def edit_distance_dp(self,s:str, t:str) -> int:
        n,m=len(s),len(t)
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            dp[i][0]=i
        for j in range(1,m+1):
            dp[0][j]=j
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    # 最少编辑步数 = 插入、删除、替换这三种操作的最少编辑步数 + 1
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        return dp[n][m]

s=Solution()
cost=[0,1,10,1]
result1=s.min_cost_climbing_stairs_dp(cost)
result2=s.climbing_stairs_dp(10)

print(result1)
print(result2)


grid=     [[1, 3, 1, 5],
           [2, 2, 4, 2],
           [5, 3, 2, 1],
           [4, 3, 5, 2]]
n,m=len(grid),len(grid[0])
res=s.min_path_sum_dfs(grid,n-1,m-1)
print(f"{res}")

mem=[[-1] * m for _ in range(n)]
result4=s.min_path_sum_dfs_mem(grid,mem,n-1,m-1)
print(f"{result4}")

result5=s.min_path_sum_dp(grid)
print(result5)

wgt = [10, 20, 30, 40, 50]
val = [50, 120, 150, 210, 240]
cap = 50
n = len(wgt)
result6=s.knapsack_dfs(wgt,val,n,cap)
print(result6)

result7=s.knapsack_dp(wgt,val,cap)
print(result7)

result8=s.unbounded_knapsack_dp(wgt,val,cap)
print(result8)

coins=[1,2,5]
result9=s.coin_change_dp(coins,11)
print(result9)

c="book"
t="code"
n,m=len(c),len(t)
result10=s.edit_distance_dp(c,t)
print(result10)

#每次遇到 0 就将其改为 2 并且累加计数器
# matrix=[list(map(int,input())) for _ in range(30)]
# res=0
#
# def dfs(i,j):
#     global res
#     matrix[i][j]=2
#     res+=1
#     for x,y in ((i+1,j),(i-1,j),(i,j-1),(i,j+1)):
#         if 0<=x<30 and 0<=y<40 and matrix[x][y]==0:
#             dfs(x,y)
#
#
# dfs(0,0)
# print(res)

#连通块问题，dfs解决（bfs也可），对于遍历过的位置置0，以防重复计算，并用一个mx记录当前最大联通块大小。最后的mx即为答案
# matrix=[list(map(int,input())) for _ in range(30)]
# mx=0
#
# def dsf2(i,j):
#     matrix[i][j]=0
#     cnt=1
#     for x,y in ((i+1,j),(i-1,j),(i,j-1),(i,j+1)):
#         if 0<=x<30 and 0<=y<60 and matrix[x][y]==1:
#             cnt+=dsf2(x,y)
#     return cnt
#
# for i in range(30):
#     for j in range(60):
#         if matrix[i][j]==1:
#             res=dsf2(i,j)
#             if res>mx:
#                 mx=res
# print(mx)

#输入 W, H, n, R = map(int, input().split())

#10进制转化为2，8，16
# bin()
# oct()
# hex()


# class Solution:
#     def tribonaci(self, n: int) -> int:
#         if n==0:
#             return 0
#
#         elif n==1 or n==2:
#             return 1
#
#         else:
#             return self.tribonaci(n-1)+self.tribonaci(n-2)+self.tribonaci(n-3)
#
# s=Solution()
# n=int(input())
# res=s.tribonaci(n)
# print(res)


#
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         return  comb(m + n - 2, n - 1)
#
# s=Solution()
# m,n=map(int,input().split())
# res=s.uniquePaths(m,n)
# print(res)





