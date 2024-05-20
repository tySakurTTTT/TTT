class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def pre_order_recur(head):
    if head is None:
        return

    print(head.value,end=" ")
    pre_order_recur(head.left)
    pre_order_recur(head.right)

def in_order_recur(head):
    if head is None:
        return

    in_order_recur(head.left)
    print(head.value,end=" ")
    in_order_recur(head.right)

def pos_order_recur(head):
    if head is None:
        return

    pos_order_recur(head.left)
    pos_order_recur(head.right)
    print(head.value,end=" ")


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

print("先序遍历:")
pre_order_recur(root)

print("\n中序遍历:")
in_order_recur(root)

print("\n后序遍历:")
pos_order_recur(root)
