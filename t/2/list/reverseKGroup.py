class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def __init__(self):
        self.tmp = None

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head

        tail=head
        for i in range(0,k):
            # 不是 k 的倍数，则保持原样，直接返回头结点
            if tail is None:
                return head
            tail=tail.next
        pre = None
        cur = head
        while cur != tail:
            temp = cur.next#保存下一个节点
            cur.next = pre#将当前节点的 next 指针指向前一个节点，实现反转。
            pre = cur#更新前一个节点为当前节点，以备下一次迭代使用
            cur = temp#将当前节点移动到下一个节点，准备进行下一次迭代。
            # ---------------------------------------反转链表
        head.next = self.reverseKGroup(tail, k)
        return pre

# 示例用法：
a = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = a.reverseKGroup(head, 2)
while result:
    print(result.value, end=" ")
    result = result.next