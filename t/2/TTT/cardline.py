def win(arr):
    if (arr is None or len(arr)==0):
        return 0
    return max(f(arr,0,len(arr)-1),s(arr,0,len(arr)-1))

def s(arr,i,j):
    if i==j:
        return arr[i]
    return max(arr[i]+s(arr,i+1,j),arr[j]+s(arr,i,j-1))

def f(arr,i,j):
    if i==j:
        return arr[i]

    return min(f(arr,i+1,j),f(arr,i,j-1))

arr=[1,9,1]
print(win(arr))
