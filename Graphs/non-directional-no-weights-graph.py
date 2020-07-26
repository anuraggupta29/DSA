import random
def assignSimpleGraph():
    g = Graph()
    g.addVertex('A')
    g.addVertex('B')
    g.addVertex('C')
    g.addVertex('D')
    g.addVertex('E')
    g.addEdge('A','B')
    g.addEdge('B','C')
    g.addEdge('B','D')
    g.addEdge('C','E')
    g.addEdge('D','E')
    return g

#Generates a Random Graph
def assignRandomGraph(chr1 = 'A', chr2 = 'G', edges = 0):
    g = Graph()
    ord1, ord2 = ord(chr1), ord(chr2)
    maxedges = (abs(ord1 - ord2))**2 - (abs(ord1 - ord2))//2
    if edges ==  0 or edges > maxedges:
        edges = abs(ord1 - ord2)
    for id in range(ord1, ord2+1):
        g.addVertex(chr(id))
    pairs = []
    while edges > 0:
        rand1 = random.randint(ord1, ord2)
        rand2 = random.randint(ord1, ord2)
        if rand1 != rand2 and (min(rand1, rand2), max(rand1, rand2)) not in pairs:
            g.addEdge(chr(rand1), chr(rand2))
            pairs.append((min(rand1, rand2), max(rand1, rand2)))
            edges -= 1
    return g

def printGraph(graph):
    details = graph.graphDetails()
    print('The Graph')
    for i in details:
        print(i, details[i])

class Vertex:
    def __init__(self, id):
        self.id = id
        self.connectedTo = []

    def addNeighbor(self, nbr):
        self.connectedTo.append(nbr)

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def printVertexConnections(self):
        allinfo = {'Vertex ID': self.id, 'Connections' : [i.id for i in self.connectedTo]}
        return allinfo

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.dfslist = []

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex

    def addEdge(self, f, t):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)

        self.vertList[f].addNeighbor(self.vertList[t])
        self.vertList[t].addNeighbor(self.vertList[f])

    def graphDetails(self):
        graphDict = {self.vertList[i].id :  [j.id for j in self.vertList[i].connectedTo] for i in self.vertList}
        return graphDict

    def dfs(self, vert):
        global dfslist
        dfslist = []
        self._dfs(self.vertList[vert])
        return dfslist, [i.id for i in dfslist]

    def _dfs(self, vert):
        global dfslist
        dfslist.append(vert)
        for v in vert.connectedTo:
            if v not in dfslist:
                self._dfs(v)

    def dfsStack(self, vert):
        dfslist = []
        stacklist = [self.vertList[vert]]
        while stacklist:
            curvert = stacklist.pop()
            if curvert not in dfslist:
                dfslist.append(curvert)
                stacklist.extend([v for v in curvert.connectedTo if v not in dfslist])
        return dfslist, [i.id for i in dfslist]

    def bfs(self, vert):
        bfslist = []
        q = [self.vertList[vert]]
        while q:
            curvert = q.pop(0)
            if curvert not in bfslist:
                bfslist.append(curvert)
                q.extend([v for v in curvert.connectedTo if v not in bfslist])
        return bfslist, [i.id for i in bfslist]

    def bfsAllPaths(self, start, goal):
        pathlist = []
        startvert = self.vertList[start]
        goalvert = self.vertList[goal]
        q = [(startvert, [startvert])]

        while q:
            (curvert, path) = q.pop(0)
            for v in curvert.connectedTo:
                if v not in path:
                    if v == goalvert:
                        pathlist.append(path+[goalvert])
                    else:
                        q.append((v, path + [v]))

        return pathlist, [[j.id for j in i] for i in pathlist]

    def bfsShortestPath(self, start, goal):
        path = None
        startvert = self.vertList[start]
        goalvert = self.vertList[goal]
        q = [(startvert, [startvert])]
        found = False

        while q and not found:
            (curvert, path) = q.pop(0)
            for v in curvert.connectedTo:
                if v not in path:
                    if v == goalvert:
                        path.append(goalvert)
                        found = True
                        break
                    else:
                        q.append((v, path + [v]))

        return path, [i.id for i in path]

mygraph = assignRandomGraph()
#mygraph = assignSimpleGraph()

printGraph(mygraph)

print('DFS Recursion List : ', mygraph.dfs('A')[1])
print('DFS Stack List : ', mygraph.dfsStack('A')[1])
print('BFS Queue List : ', mygraph.bfs('A')[1])
print('BFS Shortest Path : ', mygraph.bfsShortestPath('A','E')[1])
print('BFS All Paths : ', mygraph.bfsAllPaths('A','E')[1])
