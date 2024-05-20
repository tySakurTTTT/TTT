class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

def listpartition( head ,pivot):
    sH=None
    sT=None
    eH=None
    eT=None
    bH=None
    bT=None
    next_node=None

    while head is not None:
        next_node = head.next
        head.next = None

        if head.value < pivot:
            if sH is None:
                sH = head
                sT = head
            else:
                sT.next = head
                sT = head
        elif head.value == pivot:
            if eH is None:
                eH = head
                eT = head
            else:
                eT.next = head
                eT = head
        else:
            if bH is None:
                bH = head
                bT = head
            else:
                if head.value < bH.value:
                    head.next = bH
                    bH = head
                else:
                    current = bH
                    while current.next is not None and current.next.value < head.value:
                        current = current.next
                    head.next = current.next
                    current.next = head

        head = next_node

    if sT is not None:
        sT.next=eH
        eT=eT if eT is not None else sT

    if eT is not None:
        eT.next=bH

    return sH if sH is not None else eH if eH is not None else bH


# 创建示例链表: 1 -> 3 -> 7 -> 5 -> 2 -> 6 -> 4
head = Node(1)
head.next = Node(3)
head.next.next = Node(7)
head.next.next.next = Node(5)
head.next.next.next.next = Node(2)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(4)

# 打印原始链表
print("原始链表:")
print_linked_list(head)

# 使用list_partition_2函数分区，以3为基准
pivot_value = 3
new_head = listpartition(head, pivot_value)

# 打印分区后的链表
print(f"\n以 {pivot_value} 分区后的链表:")
print_linked_list(new_head)


