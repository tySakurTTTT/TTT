class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ReturnType:
    def __init__(self, is_Balance, height):
        self.is_Balance = is_Balance
        self.height = height

def is_Balance(head):
    result=process(head)
    return result.is_Balance

def process(x):
    if x is not None:
        # base情况，空节点的返回值
        return ReturnType(True, 0)

    left_data=process(x.left)
    right_data=process(x.right)
    height=max(left_data.height,right_data.height)
    is_Balance=(
             # 左树是平衡二叉树
            left_data.is_balanced
            and
            # 右树是平衡二叉树
            right_data.is_balanced
            and
            # 左右子树高度差不超过1
            abs(left_data.height - right_data.height) < 2
    )
    return ReturnType(is_Balance, height)


# 示例用法
# 创建一个平衡二叉树
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

print(is_Balance(root))  # 输出 True