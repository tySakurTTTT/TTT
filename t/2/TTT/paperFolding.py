def printprocess(i,n,down):
    if i>n:
        return
    printprocess(i+1,n,True)
    print("dowm" if down else "up")
    printprocess(i+1,n,False)
def all_Folding(n):
    printprocess(1,n,True)
n=3
print(all_Folding(n))
