class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None or head.next.next is None:
            return None

        slow = head.next
        fast = head.next.next

        while (slow != fast):
            if fast.next is None or fast.next.next is None:
                return None

            fast = fast.next.next
            slow = slow.next

        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow


head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2

s = Solution()
result = s.hasCycle(head)
print(result.value)
