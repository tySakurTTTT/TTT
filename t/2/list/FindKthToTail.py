class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def FindKthToTail(self,head:ListNode,k:int)->ListNode:
        fast=head
        slow=head
        for i in range(k):
            if fast ==None:
                return  None
            fast=fast.next
        while fast!=None:
            print(slow.value)
            fast=fast.next
            slow=slow.next
        return slow


solution = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = solution.FindKthToTail(head,4)
