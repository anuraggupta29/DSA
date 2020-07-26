inf = float('inf')
graph = {
'A': {'B':2, 'C':3},
'B': {'D':6, 'E':8},
'C': {'B':1, 'D':4},
'D': {'E':2, 'F':2},
'E': {'F':1},
'F': {}
}

def bellman_ford(graph, src):
    edgelist = [(i,j) for i in graph for j in graph[i]]
    shortest_path = {i:inf for i in graph.keys()}
    shortest_path[src] = 0

    for vert in range(len(graph)-1):
        changed = 0
        for edge in edgelist:
            if shortest_path[edge[0]] + graph[edge[0]][edge[1]] < shortest_path[edge[1]]:
                shortest_path[edge[1]] = shortest_path[edge[0]] + graph[edge[0]][edge[1]]
                changed += 1

        if changed == 0:
            break

    return shortest_path

print(bellman_ford(graph, 'A'))
