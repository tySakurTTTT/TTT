class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


def pre_order_unrecur(head):
    print("pre_order:",end="")
    if head is not None:
        stack=[head]
        while stack :
            #弹出一个节点
            head=stack.pop()
            print(head.value,end=" ")
            # 2.往栈加入节点，先右子节点后左子节点（如果有）
            if head.right:
                stack.append(head.right)
            if head.left:
                stack.append(head.left)
    print()

def in_order_unrecur(head):
    print("in_order::", end="")
    if head is not None:
        stack = []
        while head or stack:
            if head is not None:
                # 1. 所有的左子节点全部进栈
                stack.append(head)
                head = head.left
            else:
                # 2. 弹出栈一个节点，如果有右子节点，对右子节点周而复始上述操作
                head = stack.pop()
                print(head.value, end=" ")
                head = head.right
    print()

def pos_order_unrecur(head):
    print("pos_order:",end="")
    if head is not None:
        stack1=[head]
        stack2=[]  # 收集栈
        while stack1:
             # 1.从stack1弹出一个节点，放入收集站stack2
             head=stack1.pop()
             if head is not None:
                 stack2.append(head)
             # 2.先压左子节点进收集站，后压右子节点进收集站
             if head.left:
                 stack1.append(head.left)
             if head.right:
                 stack1.append(head.right)
        while stack2:
            print(stack2.pop().value,end=" ")
    print()

# 示例用法
# 创建一个二叉树
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

pre_order_unrecur(root)
in_order_unrecur(root)
pos_order_unrecur(root)









