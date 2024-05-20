import random

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quick_sort(arr):
    if arr is None or len(arr) < 2:
        return arr
    quick_sort_internal(arr, 0, len(arr) - 1)

def quick_sort_internal(arr, l, r):
    if l < r:
        rand_index = random.randint(l, r)
        arr[rand_index], arr[r] = arr[r], arr[rand_index]
        p = partition(arr, l, r)
        quick_sort_internal(arr, l, p[0] - 1)
        quick_sort_internal(arr, p[1] + 1, r)

def partition(arr, l, r):
    less = l - 1
    more = r
    while l < more:
        if arr[l] < arr[r]:
            less += 1
            swap(arr, less, l)
            l += 1
        elif arr[l] > arr[r]:
            more -= 1
            swap(arr, more, l)
        else:
            l += 1
    swap(arr, more, r)
    return [less + 1, more]

arr = [random.randint(0, 10000) for i in range(10)]
print("原始数组:", arr)
quick_sort(arr)
print("排序后数组:", arr)


