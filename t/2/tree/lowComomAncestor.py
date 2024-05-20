class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 方法1，递归方式
def lowest_common_ancestor(head, o1, o2):
    if not head or head == o1 or head == o2:
        return head

    left=lowest_common_ancestor(head.left,o1,o2)
    right=lowest_common_ancestor(head.right,o1,o2)
#左右2边返回值都是null，说明子节点没有o1，o2，所以返回head
    if left and right:
        return head
    return left if left else right

# 方法2，记录父节点方式
class Record1:
    def __init__(self, head):
        self.map = {}
        if head:
            self.map[head] = None
        self.set_map(head)

    def set_map(self,head):
        if not head:
            return
        if head.left:
            self.map[head.left]=head
        if head.right:
            self.map[head.right]=head
        self.set_map(head.left)
        self.set_map(head.right)

    def query(self,o1,o2):
        path=set()
        while o1 in self.map:
            path.add(o1)
            o1=self.map[o1]

        while o2 not in path:
            o2=self.map[o2]
        return o2

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

# 示例方法1的用法
o1 = root.left.left  # 节点4
o2 = root.left.right  # 节点5
result1 = lowest_common_ancestor(root, o1, o2)
print("方法1 - 最低公共祖先:", result1.value)  # 输出 2

# 示例方法2的用法
record = Record1(root)
result2 = record.query(o1, o2)
print("方法2 - 最低公共祖先:", result2.value)  # 输出 2
