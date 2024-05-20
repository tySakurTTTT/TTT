class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def is_palindrome3(head):
    if head is None or head.next is None:
        return True

    n1 = head  # 慢指针
    n2 = head  # 快指针

    # 快慢指针找末尾和中点
    while n2.next is not None and n2.next.next is not None:
        n1 = n1.next  # n1 -> mid
        n2 = n2.next.next  # n2 -> end

    n2 = n1.next  # n2 -> right part first node
    n1.next = None  # mid.next -> null

    n3 = None  # 用于记录n2原本的下一个node

    # 右半部分逆序
    while n2 is not None:
        n3 = n2.next  # n3 -> save next node，保留未改变的链表
        n2.next = n1  # next of right node convert，改变链表指向
        # n1，n2两个指针完成改变指向操作后，同时右移，准备下一个元素的链表指向逆序
        n1, n2 = n2, n3  # n1 move

    n3 = n1  # n3 -> save last node
    n2 = head  # n2 -> left first node
    res = True

    while n1 is not None and n2 is not None:
        # 每走一步，都验证
        if n1.value != n2.value:
            res = False
            break
        # n1，n2从中间开始走
        n1 = n1.next  # left to mid
        n2 = n2.next  # right to mid

    n1 = n3.next
    n3.next = None

    # 最后将逆序的链表变回来
    while n1 is not None:
        n2 = n1.next
        n1.next = n3
        n3 = n1
        n1 = n2

    return res

# 示例用法:
# 创建链表
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

# 检查是否为回文
result = is_palindrome3(head)
print(result)
