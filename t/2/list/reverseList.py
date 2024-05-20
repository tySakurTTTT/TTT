class ListNode:
        def __init__(self,value=0,next=None):
            self.value=value
            self.next=next

class Solution:
    def reverseList(self,head:ListNode)->ListNode:#递归
        if head is None or head.next is None:
            return head

        cur=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return cur

    def reverseList2(self, head: ListNode) -> ListNode:  # 非递归
        if head is None or head.next is None:
            return head

        p=head
        q=None
        while p:
            tmp=p.next
            p.next=q
            q=p
            p=tmp
        return q

head=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
s=Solution()
result=s.reverseList(head)
while result:
    print(result.value,end=" ")
    result=result.next
print(" ")
result2=s.reverseList2(head)
while result2:
    print(result2.value,end=" ")
    result2=result2.next