import random
def merge_sort(list):
    if len(list)<=1:
        return list

    mid=int(len(list)/2)
    left=merge_sort(list[:mid])
    right=merge_sort(list[mid:])
    return merge(left,right)

def merge(left,right):
    res=[]
    i=j=k=0
    while(i<len(left) and j<len(right)):
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right                [j])
            j+= 1
    res=res+left[i:]+right[j:]
    return res

list=[random.randint(0,10000) for i in range(10)]
print(list)
print(merge_sort(list))


def merge_sort(arr):
    if arr is None or len(arr) < 2:
        return
    merge_sort_helper(arr, 0, len(arr) - 1)

def merge_sort_helper(arr, l, r):
    if l < r:
        mid = l + (r - l) // 2
        merge_sort_helper(arr, l, mid)
        merge_sort_helper(arr, mid + 1, r)
        merge(arr, l, mid, r)

def merge(arr, l, m, r):
    help_arr = [0] * (r - l + 1)
    i = 0
    p1, p2 = l, m + 1
    while p1 <= m and p2 <= r:
        help_arr[i] = arr[p1] if arr[p1] < arr[p2] else arr[p2]
        i += 1
        if arr[p1] < arr[p2]:
            p1 += 1
        else:
            p2 += 1

    while p1 <= m:
        help_arr[i] = arr[p1]
        i += 1
        p1 += 1

    while p2 <= r:
        help_arr[i] = arr[p2]
        i += 1
        p2 += 1

    for i in range(len(help_arr)):
        arr[l + i] = help_arr[i]

# 示例用法:
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
merge_sort(arr)
print(arr)





















