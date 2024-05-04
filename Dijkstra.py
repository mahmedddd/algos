import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# Example usage:
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'D': 6, 'E': 2},
    'C': {'A': 3, 'F': 8},
    'D': {'B': 6},
    'E': {'B': 2, 'F': 4},
    'F': {'C': 8, 'E': 4}
}

start_node = 'A'
print("Shortest distances from node", start_node, "using Dijkstra's Algorithm:")
print(dijkstra(graph, start_node))
