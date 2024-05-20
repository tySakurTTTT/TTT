class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
   def merge(self,head1:ListNode,head2:ListNode)->ListNode:
       if head1 is None:
           return  head2
       if head2 is None:
           return head1

       if head1.value<=head2.value:
           head1.next=self.merge(head1.next,head2)
           return  head1
       if head1.value >=head2.value:
           head2.value=self.merge(head1,head2.next)
           return   head2

# 示例用法：
a = Solution()
head1= ListNode(1, ListNode(3, ListNode(5 )))
head2= ListNode(2, ListNode(4, ListNode(6 )))
result = a.merge(head1,head2)
while result :
    print(result.value, end=' ')
    result = result.next

