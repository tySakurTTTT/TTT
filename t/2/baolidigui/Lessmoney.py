import heapq
def less_money(arr):
    heapq.heapify(arr)
    sum_result=0
    while len(arr)>1:
        cur=heapq.heappop(arr)+heapq.heappop(arr)
        sum_result+=cur
        heapq.heappush(arr,cur)
    return sum_result

# Example usage:
arr = [3, 1, 2, 6]
result = less_money(arr)
print(result)