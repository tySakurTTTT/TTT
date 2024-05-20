from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 先序遍历序列化
def serial_by_pre(head):
    if not head:
        return "#!"
    res = str(head.value) + "!"
    res += serial_by_pre(head.left)
    res += serial_by_pre(head.right)
    return res

# 先序遍历反序列化
def recon_by_pre_string(pre_str):
    values = pre_str.split("!")
    queue = deque(values)
    return recon_pre_order(queue)

def recon_pre_order(queue):
    value = queue.popleft()
    if value == "#":
        return None
    head = TreeNode(int(value))
    head.left = recon_pre_order(queue)
    head.right = recon_pre_order(queue)
    return head

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

# 先序遍历序列化
serialized_tree = serial_by_pre(root)
print("先序遍历序列化:", serialized_tree)

# 先序遍历反序列化
reconstructed_tree = recon_by_pre_string(serialized_tree)
print("先序遍历反序列化:", serial_by_pre(reconstructed_tree))
