class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


def is_BST(head):
    if head is not None:
        return True
    in_order_list=[]
    # 保留中序次序
    process(head,in_order_list)

    pre=float('-inf')
    # 遍历中序次序，看是否由小到大
    for cur in in_order_list:
        if pre>cur.value:
            return False
        pre=cur.value
    return True


# 递归中序遍历，把原来的打印换成把节点添加到新列表，保留中序次序
def process(node, in_order_list):
    if node is None:
        return

    process(node.left, in_order_list)
    in_order_list.append(node)
    process(node.right, in_order_list)

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


print(is_BST(root))

###黑盒方法
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class ReturnType:
    def __init__(self, isBST, _min, _max):
        self.isBST = isBST
        self.min = _min
        self.max = _max


def is_bst_1(head):
    result = process(head)
    return result.isBST


def process(x):
    if x is None:
        # base情况，空节点的返回值
        return None

    left_data = process(x.left)
    right_data = process(x.right)

    _min = x.value
    _max = x.value

    # 先用子树的最大最小值更新此节点的最大最小值
    if left_data is not None:
        _min = min(_min, left_data.min)
        _max = max(_max, left_data.max)

    if right_data is not None:
        _min = min(_min, right_data.min)
        _max = max(_max, right_data.max)

    is_bst = True

    # 判断子树是否违规
    # 违规条件1：左子树存在，且它的最大值大于父节点或者
    # 左子树不是搜索二叉树
    if left_data is not None and (not left_data.isBST or left_data.max >= x.value):
        is_bst = False

    # 违规条件2：右子树存在，且它的最小值小于父节点或者
    # 右子树不是搜索二叉树
    if right_data is not None and (not right_data.isBST or right_data.min <= x.value):
        is_bst = False

    return ReturnType(is_bst, _min, _max)


# 示例用法
# 创建一个二叉搜索树
#       2
#      / \
#     1   3

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(is_bst_1(root))  # 输出 True
