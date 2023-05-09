path = []
prev = {}
graph = {
    'AB_XY': ['_ABXY', 'A_BXY'],
    '_ABXY': [],
    'A_BXY': ['_ABXY', 'AXB_Y'],
    '_ABXY': [],
    'AXB_Y': ['AXBY_', 'AX_BY'],
    'AXBY_': ['AX_YB'],
    'AX_BY': ['_XABY', 'AXBY_'],
    'AXBY_': ['AX_YB'],
    '_XABY': ['X_ABY'],
    'AX_YB': ['_XAYB', 'AXY_B'],
    'X_ABY': [],
    '_XAYB': ['X_AYB'],
    'AXY_B': [],
    'X_AYB': ['XYA_B'],
    'XYA_B': ['XY_AB'],
    'XY_AB': []
}

def dfs(graph, start, goal):
    path = set()
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        print(stack)
        path.add(node)
        if node == goal:
            break
        visited.add(node)
        for i in graph[node]:
            stack.append(i)
    print("path is",path)
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
def IDS(graph, start, goal):
    for x in range(2, 15):
        print("Iterative deeping ", x)
        dfsbounded(graph, start, goal, x)
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
IDS(graph, 'AB_XY', 'XY_AB')