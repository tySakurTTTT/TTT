from queue import Queue


class Node:
    def __init__(self, value):
        self.value = value
        self.nexts = []


class Graph:
    def __init__(self):
        self.nodes = {}


def bfs(start_node):
    if start_node is None:
        return

    # 用来储存所有节点
    queue = Queue()
    # 确保上面的队列储存的节点不要重复
    visited = set()

    queue.put(start_node)
    visited.add(start_node)

    while not queue.empty():
        cur = queue.get()
        print(cur.value)

        for next_node in cur.nexts:
            # 不重复，则添加到队列和set中
            if next_node not in visited:
                visited.add(next_node)
                queue.put(next_node)


# 示例用法：
# 假设 graph 是你的图对象，start_node 是开始的节点
# 创建图
graph = Graph()
# 添加节点
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
# 连接节点
node1.nexts = [node2, node3]
node2.nexts = [node1, node3]
node3.nexts = [node1, node2]

# 将节点添加到图中
graph.nodes[1] = node1
graph.nodes[2] = node2
graph.nodes[3] = node3

# 从某个节点开始进行 BFS
start_node = graph.nodes[1]
bfs(start_node)
