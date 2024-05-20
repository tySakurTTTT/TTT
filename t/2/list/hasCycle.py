class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return None

        slow = head.next
        fast = head.next.next

        while slow != fast:
            if fast.next is None or fast.next.next is None:
                return None

            slow = slow.next
            fast = fast.next.next

        # Reset one pointer to the head
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

# Example
# Create a linked list with a cycle
head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2  # Cycle: 5 -> 2

solution = Solution()
result = solution.hasCycle(head)
print(result.value)  # Output: 2
