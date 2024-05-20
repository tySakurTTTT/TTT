class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


def get_successor_node(node):
    if not node:
        return None

    if node.right:
    # 右子节点不为空，则后继节点必为右子节点子树的最左节点
        parent=node.parent
        return get_left_most(node.right)

    else:
# 右子节点为空，一直往上找父节点，直到父节点不为别人的右子节点
          parent = node.parent
          while parent and parent.right==node:
              node=parent
              parent=node.parent
          return parent

def get_left_most(node):
    if not node:
        return None

    while node.left:
        node=node.left

    return node

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

# 设置父节点指针
root.left.parent = root
root.right.parent = root
root.left.left.parent = root.left
root.left.right.parent = root.left

# 示例用法
successor_node = get_successor_node(root.left.left)  # 获取节点4的后继节点
print("后继节点:", successor_node.value)  # 输出 2
