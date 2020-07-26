inf = float('inf')
graph = {
'A': {'B':2, 'C':3},
'B': {'D':6, 'E':8},
'C': {'B':1, 'D':4},
'D': {'E':2, 'F':2},
'E': {'F':1},
'F': {}
}

def dijkstra(graph, src):
    shortest_path = {i:inf for i in graph.keys()}
    shortest_path[src] = 0
    not_visited = {'A':0}

    while not_visited:
        cur_min = min(not_visited, key=lambda x: not_visited[x])
        cur_min_val = not_visited.pop(cur_min)
        for vert in graph[cur_min]:
            if shortest_path[cur_min] + graph[cur_min][vert] < shortest_path[vert]:
                shortest_path[vert] = shortest_path[cur_min] + graph[cur_min][vert]
                not_visited[vert] = shortest_path[vert]

    return shortest_path

print(dijkstra(graph, 'A'))
