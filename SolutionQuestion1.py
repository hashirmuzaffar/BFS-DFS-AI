path = []
prev = {}
graph = {
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Zerind': ['Arad', 'Odarea'],
    'Odarea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Odarea', 'Arad', 'Rimnicu Vilcea', 'Farara'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Dobreta'],
    'Dobreta': ['Mehadia', 'Craiova'],
    'Craiova': ['Dobreta', 'Rimnicu Vilcea'],
    'Rimnicu Vilcea': ['Craiova', 'Sibiu'],
    'Farara': ['Sibiu', 'Bucharest'],
    'Bucharest': ['Farara', 'Giurgui', 'Urziceni'],
    'Giurgui': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova'],
    'Hirsova': ['Urziceni', 'Eforie', 'Vaslui'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}
def dfs(graph, start, goal):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        print(node)
        if node == goal:
            break
        visited.add(node)
        for i in graph[node]:
            stack.append(i)
def dfsbounded(graph, start, goal, bound):
    visited = set()
    stack = [start]
    while len(stack) <= bound and stack:
        node = stack.pop()
        if node in visited:
            continue
        print(node)
        if node == goal:
            break
        visited.add(node)
        for i in graph[node]:
            stack.append(i)
def IDS(graph, start):
    for x in range(2, 15):
        print("Iterative deeping ", x)
        dfsbounded(graph, start, x)
def bfs(graph, start, goal):
    visited = set()
    queue= []
    queue.append(start)
    visited.add(start)
    while queue:
        node = queue.pop(0)
        for x in graph[node]:
            if x not in visited:
                visited.add(x)
                prev[x] = node
                queue.append(x)
    x = goal
    while x != start:
        path.append(x)
        x = prev.get(x)
    path.append(x)
    path.reverse()
    print(path)

bfs(graph, 'Arad', 'Bucharest')