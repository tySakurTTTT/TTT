def find(parent, vertex):
    if parent[vertex] == vertex:
        return vertex
    return find(parent, parent[vertex])


def union(parent, rank, vertex1, vertex2):
    root1 = find(parent, vertex1)
    root2 = find(parent, vertex2)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1


def kruskal_algorithm(graph):
    # 初始化结果
    minimum_spanning_tree = []

    # 初始化并查集
    parent = {vertex: vertex for vertex in graph.keys()}
    rank = {vertex: 0 for vertex in graph.keys()}

    # 获取所有的边
    edges = []
    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            edges.append((vertex, neighbor, weight))

    # 按权值排序边
    edges.sort(key=lambda edge: edge[2])

    # 不断取出权值最小的边并判断是否形成环
    for edge in edges:
        vertex1, vertex2, weight = edge
        if find(parent, vertex1) != find(parent, vertex2):
            union(parent, rank, vertex1, vertex2)
            minimum_spanning_tree.append(edge)

        if len(minimum_spanning_tree) == len(graph) - 1:
            break

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

result = kruskal_algorithm(graph)
print(result)