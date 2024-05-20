def hanoi(n):
    if (n>0):
        func(n,"左","右","中")
def func(i,start,end,other):
    if (i==1):
        print("move 1 from "+start+" to "+end)
    else:
        func(i-1,start,other,end)
        print("move "+str(i)+" from "+start+" to "+end)
        func(i-1,other,end,start)


if __name__=="__main__":
    n=3
    hanoi(n)
