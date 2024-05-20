class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.visited = False

def dfs(node):
    if not node:
        return

    print(node.value)
    node.visited = True

    for neighbor in node.neighbors:
        if not neighbor.visited:
            dfs(neighbor)

# 示例用法:
# 创建节点
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# 定义边（连接节点）
node1.neighbors = [node2, node3]
node2.neighbors = [node1, node4]
node3.neighbors = [node1]
node4.neighbors = [node2]

# 从node1开始执行DFS
print("从node1开始的DFS:")
dfs(node1)
