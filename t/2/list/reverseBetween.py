class ListNode:
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next
class Solution:
    def ReverseBetween(self, head: ListNode,m:int,n:int) -> ListNode:
        if head is None:
           return head

        res=ListNode(-1)
        res.next=head
        pre=res
        cur=head
        for i in range(1,m):
            pre=cur
            cur=cur.next

        for i in range(m,n+1):
            tmp=cur.next
            cur.next=tmp.next
            tmp.next=pre.next
            pre.next=tmp

        return res.next
    def link(self,head:ListNode)->None:
        cur=head
        while cur:
           print(cur.value,end=" ")
           cur=cur.next
        print( )



head=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
s=Solution()

s.link(head)

print(" ")
reversed_head=s.ReverseBetween(head,2,4)
s.link(reversed_head)

