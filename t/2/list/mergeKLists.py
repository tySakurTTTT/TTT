from typing import List
from queue import PriorityQueue

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pq = PriorityQueue()
        for i in range(len(lists)):
            if lists[i]:
                pq.put((lists[i].value, i))
                lists[i] = lists[i].next

        res = ListNode(-1)
        head = res
        while not pq.empty():
            val, index = pq.get()
            head.next = ListNode(val)
            head = head.next
            if lists[index]:
                pq.put((lists[index].value, index))
                lists[index] = lists[index].next
        return res.next

# Helper function to convert a list to a ListNode
def list_to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to convert a ListNode to a list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.value)
        node = node.next
    return result

# Example 1
lists1 = [list_to_linked_list([1, 4, 5]), list_to_linked_list([1, 3, 4]), list_to_linked_list([2, 6])]
solution1 = Solution()
result1 = solution1.mergeKLists(lists1)
print(linked_list_to_list(result1))
# Output: [1, 1, 2, 3, 4, 4, 5, 6]

# Example 2
lists2 = [list_to_linked_list([1, 2, 3]), list_to_linked_list([]), list_to_linked_list([4, 5])]
solution2 = Solution()
result2 = solution2.mergeKLists(lists2)
print(linked_list_to_list(result2))
# Output: [1, 2, 3, 4, 5]

# Example 3
lists3 = []
solution3 = Solution()
result3 = solution3.mergeKLists(lists3)
print(linked_list_to_list(result3))
# Output: []
