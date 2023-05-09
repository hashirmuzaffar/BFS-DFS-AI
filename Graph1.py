adj_list = {}
mylist = []
size = 0
goal = ''
start = ''
Matric_with_ones = []
Matric_with_weights = []
bfs_path = []
dfs_path = []
dfscost = 0
cost = []
bfs_cost = 0

def reset():
    mylist.clear()
    adj_list.clear()
    Matric_with_weights.clear()
    Matric_with_ones.clear()
    dfs_path.clear()
    bfs_path.clear()
    bfs_cost = 0
    dfscost = 0
    prev.clear()
    path.clear()

def add_edge(node1, node2, weight):
    if node1 not in mylist and node2 not in mylist:
        mylist.append(node1)
        mylist.append(node2)
    elif node1 not in mylist and node2 in mylist:
        mylist.append(node1)
    elif node2 not in mylist and node1 in mylist:
        mylist.append(node2)

    temp = []
    if node1 in mylist and node2 in mylist:
        if node1 not in adj_list:
            temp2 = []
            temp2.append(node2)
            temp2.append(weight)
            temp.append(temp2)
            adj_list[node1] = temp

        elif node1 in adj_list:
            temp.extend(adj_list[node1])
            temp2 = []
            temp2.append(node2)
            temp2.append(weight)
            temp.append(temp2)
            adj_list[node1] = temp

    else:
        print("Nodes don't exist!")



def MatrixZero(x):
    Max = []
    for i in range(0,x):
        temp = []
        for j in range(0, x):
            temp.append(0)
        Max.append(temp)
    return Max


def Adj_to_mat_with_weights(size):
    matric = []
    matric = MatrixZero(size)
    for node in adj_list:
        for i in adj_list[node]:
            matric[ord(node)-65][ord(i[0])-65] = int(i[1])
    return matric

def Adj_to_mat_of_ones(size):
    matric = []
    matric = MatrixZero(size)
    for node in adj_list:
        for i in adj_list[node]:
            matric[ord(node)-65][ord(i[0])-65] = 1
    return matric




def dfs(graph, start, goal):
    dfscost=0
    visited = set()
    stack = [start]
    dfscost=dfscost+int(start[1])
    while stack:
        node = stack.pop()
        if node[0] in visited:
            continue
        temp=[]
        temp.append(node[0])
        dfscost=dfscost+ int(node[1])
        temp.append(dfscost)
        dfs_path.append(temp)
        if node[0] == goal:
            break
        visited.add(node[0])
        for i in graph[node[0]]:
            stack.append(i)
    str_="DFS Path is:\n ["
    for m in dfs_path:
        str_ = str_ + str(m) + ","
    str_ = str_ + "]\n Cost : " + str(dfscost)
    return str_


prev= {}
path =[]

def bfs(graph, start, goal):
    visited = set()
    queue= []
    queue.append(start)
    visited.add(start[0])
    while queue:
        node = queue.pop(0)
        for x in graph[node[0]]:
            if x[0] not in visited:
                visited.add(x[0])
                prev[x[0]] = node
                queue.append(x)
    x = goal
    bfs_cost=0
    while x[0] != start[0]:
        path.append(x[0])
        cost.append(bfs_cost)
        x = prev.get(x[0])
        bfs_cost = bfs_cost + int(x[1])
    path.append(x[0])
    cost.append(bfs_cost)
    path.reverse()
    String="\nBFS Path is:\n ["
    for w in range (len(path)):
        String= String + "["+str(path[w])+","+str(cost[w])+"],"
    String= String + "] \n Cost:" + str(bfs_cost)
    return String

def write_to(obj):
    obj.write("Graph\n")  # print Heading
    obj.write('Adjacency matrix\n')#print Heading
    string=" "
    for z in mylist:#print A B C D E ...
        string = string + str(z) + "  "
    string=string+"\n"
    obj.write(string)
    Matric_with_ones = Adj_to_mat_of_ones(size)#create Matric
    for j in range(size):#printing matric
        obj.write(str(mylist[j])+str(Matric_with_ones[j])+"\n")#printing matric
    obj.write('Costs\n')#printing matric
    string=" "#printing matric
    for z in mylist:#printing A B C D E ...
        string = string +str(z) + "  "
    string=string+"\n"
    obj.write(string)
    Matric_with_weights = Adj_to_mat_with_weights(size)#Create Martic
    for j in range(size):#printing matric
        obj.write(str(mylist[j])+str(Matric_with_weights[j])+"\n")#printing matric
    Start = [start,0]#printing matric
    obj.write(dfs(adj_list, Start, goal))#printing dfs
    obj.write(bfs(adj_list, Start, goal))






file = open("file.txt", "r")
f = file.readlines()

for line in f:
    line = line.strip()
    if "\\" in line:
        continue
    else:
        if len(line)<=2 and len(line)>0:
            size=int(line)
        elif len(line)<4 and len(line)>2:
            I=line.split()
            start = I[0]
            goal = I[1]
        elif len(line)<7 and len(line)>4:
            X=line.split()
            add_edge(X[0],X[1],X[2])
            add_edge(X[1], X[0], X[2])

output_file = open("GraphOutput1","w")
write_to(output_file)

reset()

file = open("file2.txt", "r")
f = file.readlines()

for line in f:
    line = line.strip()
    if "\\" in line:
        continue
    else:
        if len(line)<=2 and len(line)>0:
            size=int(line)
        elif len(line)<4 and len(line)>2:
            I=line.split()
            start = I[0]
            goal = I[1]
        elif len(line)<7 and len(line)>4:
            X=line.split()
            add_edge(X[0],X[1],X[2])
            add_edge(X[1], X[0], X[2])

output_file = open("GraphOutput2","w")
write_to(output_file)

reset()

file = open("file3.txt", "r")
f = file.readlines()

for line in f:
    line = line.strip()
    if "\\" in line:
        continue
    else:
        if len(line)<=2 and len(line)>0:
            size=int(line)
        elif len(line)<4 and len(line)>2:
            I=line.split()
            start = I[0]
            goal = I[1]
        elif len(line)<7 and len(line)>4:
            X=line.split()
            add_edge(X[0],X[1],X[2])
            add_edge(X[1], X[0], X[2])

output_file = open("GraphOutput3","w")
write_to(output_file)