def prim_algorithm(graph):
    num_vertices = len(graph)

    # 初始化集合
    selected = set()
    selected.add(list(graph.keys())[0])  # 从第一个顶点开始
    unselected = set(graph.keys()) - selected

    # 初始化最小生成树结果
    minimum_spanning_tree = []

    while unselected:
        min_weight = float('inf')
        start_vertex = None
        end_vertex = None

        # 遍历已选集合中的每个顶点
        for vertex in selected:
            # 遍历未选集合中的每个顶点
            for neighbor, weight in graph[vertex].items():
                if neighbor in unselected:
                    # 找到权值最小的边
                    if min_weight > weight:
                        min_weight = weight
                        start_vertex = vertex
                        end_vertex = neighbor

        # 将找到的最小权值边添加到最小生成树结果中
        minimum_spanning_tree.append((start_vertex, end_vertex, min_weight))
        selected.add(end_vertex)
        unselected.remove(end_vertex)

    return minimum_spanning_tree


graph = {
    'A': {'B': 2, 'C': 9},
    'B': {'A': 2, 'D': 4, 'E': 8},
    'C': {'A': 9, 'E': 10, 'F': 3},
    'D': {'B': 4, 'E': 1, 'G': 5},
    'E': {'B': 8, 'C': 10, 'D': 1, 'F': 11, 'G': 6, 'H': 12},
    'F': {'C': 3, 'E': 11, 'H': 17},
    'G': {'D': 5, 'E': 6},
    'H': {'E': 12, 'F': 17},
}

result = prim_algorithm(graph)
print(result)