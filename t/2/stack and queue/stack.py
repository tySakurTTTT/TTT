class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class LinkedListStack:
    def __init__(self):
        self._peek:ListNode | None=None
        self._size: int=0

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return not self._peek

    def push(self,val:int) -> None:
        #入栈
        node=ListNode(val)
        node.next=self._peek
        self._peek=node
        self._size+=1

    def pop(self) -> int:
        #出栈
        num=self._peek.val
        self._peek=self._peek.next
        self._size-=1
        return num

    def peek(self) -> int:
        if self.is_empty():
            raise indexError("Stack is empty")
        return self._peek.val

    def to_list(self)->int:
        arr=[]
        node=self._peek
        while node:
            arr.append(node.val)
            node=node.next
        arr.reverse()
        return arr


# Python 没有内置的栈类，可以把 list 当作栈来使用
stack = LinkedListStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack)

peek = stack.peek()
print(peek)

pop=stack.pop()
print(pop)
print(stack)

size=stack.size()
print(size)

is_empty=stack.is_empty()
print(is_empty)