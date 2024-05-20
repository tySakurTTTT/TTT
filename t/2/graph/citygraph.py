class Node:
    def __init__(self,value):
        self.value=value
        self.in_degree=0
        self.out_degree=0
        self.nexts=[]
        self.edges=[]

class Edge:
    def __init__(self,weight,from_node,to_node):
        self.weight = weight
        self.from_node = from_node
        self.to_node = to_node

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = set()

class GraphGenerator:
    #/matrix的每一行结构为：源城市编号，目标城市编号，距离将它转换为我的图结构表示
    @staticmethod
    def create_graph(matrix):
        graph=Graph()
        for i in range(len(matrix)):
            weight=matrix[i][0]
            from_city=matrix[i][1]
            to_city=matrix[i][2]

            if from_city not in graph.nodes:#//如果源城市第一次出现，则加入到图中，创立新节点
                graph.nodes[from_city] = Node(from_city)
            if to_city not in graph.nodes:
                graph.nodes[to_city] = Node(to_city)

            from_node = graph.nodes[from_city]#//源城市节点
            to_node = graph.nodes[to_city]

            #//创建源城市与目标城市之间的边
            new_edge = Edge(weight, from_node, to_node)

            #//完善源城市节点信息
            from_node.nexts.append(to_node)
            from_node.out_degree += 1
            from_node.edges.append(new_edge)
            to_node.in_degree += 1

            graph.edges.add(new_edge)

        return graph


matrix = [
            [10, 1, 2],
            [15, 2, 3],
            [20, 1, 3],

        ]

my_graph = GraphGenerator.create_graph(matrix)
print(my_graph)
#图生成器（GraphGenerator）的create_graph方法将输入的邻接矩阵转换为图的表示。
# 在Python中，我们使用字典和集合来模拟Java中的HashMap和HashSet的功能。