class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
    #
    # def __init__(self, val: int):
    #     self.val: int = val  # 节点值
    #     self.next: ListNode | None = None  # 指向后继节点的引用
    #     self.prev: ListNode | None = None  # 指向前驱节点的引用

def insert(n0:ListNode,p:ListNode) ->ListNode:
    if p==None:
        return
    n1=n0.nextiiii
    p.next=n1
    n0.next=p

def find(head:ListNode,target:int)->int:
    if head==None:
        return
    index=0
    while head:
        if head.val==target:
            return index
        head=head.next
        index=index+1
    return -1

if __name__ == '__main__':
    n0 = ListNode(1)
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(5)
    n4 = ListNode(4)
    # 构建节点之间的引用
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4

    p=ListNode(0)
    index=insert(n0,p)
    print(index)
    index=find(n0,2)
    print(index)

#列表
num:int=nums[1]
nums[1]=0
#清空
nums.clear()

#尾部添加
nums.append()

#中间插入
nums.insert()

#删除元素
nums.pop()