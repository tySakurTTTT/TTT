from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_cbt(head):
    if head is None:
        return True

    queue = deque()
    leaf = False  # 用来记录是否出现过某个节点左右子节点不全的情况
    l = None
    r = None
    queue.append(head)

    while queue:
        head = queue.popleft()
        l = head.left
        r = head.right

        if (
                # 情况二，在不违反情况一的条件下，在首次出现
                # 某个节点左右子节点不全的情况后，后续节点必
                # 须都是叶节点，如果不满足，则返回 False
                (leaf and (l is not None or r is not None))

                or

                # 情况一：右节点存在，左节点不存在，返回 False
                (l is None and r is not None)
        ):
            return False

        if l is not None:
            queue.append(l)
        if r is not None:
            queue.append(r)
        else:
            # 情况二，在不违反情况一的条件下，在首次出现
            # 某个节点左右子节点不全的情况后，标记事件
            leaf = True

    return True


# 示例用法
# 创建一个完全二叉树
#       1
#      / \
#     2   3
#    / \ /
#   4  5 6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

print(is_cbt(root))  # 输出 True
