def bfs(graph, goal, root):
    #used for finding the shortest path in an unweighted graph
    queue = []
    discovered = []
    parents = {}
    discovered.append(root)
    queue.append(root)
    while len(queue) > 0:
        vertex = queue.pop(0)
        if vertex == goal:
            route = []
            while vertex != root:
                route.insert(0, vertex)
                vertex = parents[vertex]
            route.insert(0, root)
            return route
        for i in graph[vertex]:
            if i not in discovered:
                queue.append(i)
                discovered.append(i)
                parents[i] = vertex
    return None

def dfs(graph, vertex, visited=[]):
    #used for navigating a maze
    visited.append(vertex)
    print(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)













graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
        }

print(bfs(graph, "d", "e"))
dfs(graph, "a")