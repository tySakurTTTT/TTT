def qiuyu(data):
    cnt=0
    for i in range(1,data+1):
        if data%i==0:
            cnt+=1
    return cnt

grid=[
[393353,901440,123481,850930,423154,240461],
[373746,232926,396677,486579,744860,468782],
[941389,777714,992588,343292,385198,876426],
[483857,241899,544851,647930,772403,109929],
[882745,372491,877710,340000,659788,658675],
[296521,491295,609764,718967,842000,670302]
]

#初始化行列n,m，dp表
n,m=len(grid),len(grid[0])
data=[[0]*n for _ in range(m)]
mx_data,mx_num=0,0

for i in range(6):
    data[i]=grid[i]
#用双循环将约数最多的数取出来，再通过max去最大的那个
for i in range(6):
    for j in range(6):
            res=qiuyu(data[i][j])
            if res>mx_num:
                mx_num=res
                mx_data=data[i][j]
print(mx_data)
print(mx_num)
