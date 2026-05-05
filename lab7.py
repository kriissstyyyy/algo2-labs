from collections import defaultdict, deque


def bfs(graph, source, sink, parent):
    visited = {source}
    queue = deque([source])

    while queue:
        node = queue.popleft()
        for neighbor, capacity in graph[node].items():
            if neighbor not in visited and capacity > 0:
                visited.add(neighbor)
                parent[neighbor] = node
                if neighbor == sink:
                    return True
                queue.append(neighbor)
    return False


def edmonds_karp(graph, source, sink):
    max_flow = 0

    while True:
        parent = {}
        if not bfs(graph, source, sink, parent):
            break

        path_flow = 10**9
        node = sink
        while node != source:
            prev = parent[node]
            path_flow = min(path_flow, graph[prev][node])
            node = prev

        node = sink
        while node != source:
            prev = parent[node]
            graph[prev][node] -= path_flow
            graph[node][prev] += path_flow
            node = prev

        max_flow += path_flow

    return max_flow


def build_graph(edges):
    graph = defaultdict(lambda: defaultdict(int))
    for u, v, capacity in edges:
        graph[u][v] += capacity
        if v not in graph or u not in graph[v]:
            graph[v][u] += 0
    return graph


def read_roads_csv(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    farms = [x.strip() for x in lines[0].split(",")]
    shops = [x.strip() for x in lines[1].split(",")]

    edges = []
    for line in lines[2:]:
        parts = [x.strip() for x in line.split(",")]
        if len(parts) != 3:
            raise ValueError(f"Неправильний формат рядка: '{line}'")
        u, v, cap = parts[0], parts[1], int(parts[2])
        edges.append((u, v, cap))

    return farms, shops, edges


def compute_max_flow(filepath):
    farms, shops, edges = read_roads_csv(filepath)
    graph = build_graph(edges)

    super_source = "__SOURCE__"
    super_sink = "__SINK__"

    for farm in farms:
        graph[super_source][farm] = 10**9
        graph[farm][super_source] = 0

    for shop in shops:
        graph[shop][super_sink] = 10**9
        graph[super_sink][shop] = 0

    return edmonds_karp(graph, super_source, super_sink)
