from collections import deque


def find_unreachable_cities(cities, storages, pipes):
    graph = {node: [] for node in (cities + storages)}
    for start, end in pipes:
        if start in graph:
            graph[start].append(end)

    results = []

    for storage in storages:
        visited = {storage}
        queue = deque([storage])

        while queue:
            current = queue.popleft()
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        unreachable = [city for city in cities if city not in visited]

        if unreachable:
            results.append([storage, unreachable])

    return results

