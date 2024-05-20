def dfs(nums: list[int], target: int, i: int, j: int) -> int:
    """二分查找：问题 f(i, j)"""
    if i>j:
        return -1
    m=(i+j)//2
    if nums[m]<target:
        return dfs(nums, target,m+1,j)
    if nums[m]>target:
        return dfs(nums,target,i,m-1)
    else:
        return m

def binary_search(nums: list[int], target: int) -> int:
    n=len(nums)
    return dfs(nums, target, 0, n-1)

if __name__ == '__main__':
    target=6
    nums=[1, 3, 6, 8, 12, 15, 23, 26, 31, 35]
    index=binary_search(nums, target)
    print(index)