# class Node:
#     def __init__(self,item):
#         self.item=item
#         self.next=None
#
# def creat_linklist_head(li):
#     head=Node(li[0])
#     for element in li[1:]:
#         node=Node(element)
#         node.next=head
#         head=node
#     return head
#
# def creat_linklist_tail(li):
#     head=Node(li[0])
#     tail=head
#     for element in li[1:]:
#         node=Node(node)
#         tail.next=node
#         node=tail
#     return    head
#
#
# def print_linklist(li):
#     while li:
#         print(li.item,end=",")
#         li=li.next
#
#
# li=creat_linklist_head([1,2,3])



class Node(object):
    def __init__(self,elem):
        self.elem=elem
        self.next=None


class SingleLinkedList:
    def is_empty(self):
        return self._head==None

    def __init__(self,node=None):
        if node!=None:
            headNode=Node(node)
            self._head=headNode
        else:
            self._head=node

    def length(self):
        count=0
        cur=self._head
        while cur!=None:
            count+=1
            cur=cur.next
            return count

    def travel(self):
        cur=self._head
        while cur!=None:
            print(cur.elem,end="\t")
            cur=cur.next
        print(" ")

    def add(self,item):
        node=Node(item)
        node.next=self._head
        self._head=None

    def append(self,item):
        node=Node(item)
        if self.is_empty():
            self._head=None
        else:
            cur=self._head
            while cur.next!=None:
                cur=cur.next
            cur.next=node



if __name__=="__main__":
    #初始化元素值为10单向链表
    singleLinkedList=SingleLinkedList([30,1,5,6,8])
    print("是否为空链表：",singleLinkedList.is_empty())
    print("链表长度为：",singleLinkedList.length())
    print("----遍历链表----")
    singleLinkedList.travel()
    print("-----头部插入-----")
    singleLinkedList.add(1)
    singleLinkedList.add(2)
    singleLinkedList.add(3)
    singleLinkedList.travel()
    print("-----尾部追加-----")
    singleLinkedList.append(10)
    singleLinkedList.append(20)
    singleLinkedList.travel()