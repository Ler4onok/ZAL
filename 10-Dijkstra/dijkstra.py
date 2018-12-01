import numpy as np

class Vertex:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.minDistance = np.inf
        self.previousVertex = None
        self.edges = []

class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


class PriorityQueue:
    def __init__(self):
        self.head = None

    class Node():
        def __init__(self, data):
            self.data = data
            self.next = None

    def push(self, data): #push to queue
        new_node = self.Node(data)
        temp = self.head
        if temp == None: #fill the head
            self.head = new_node
        elif temp.data.minDistance > new_node.data.minDistance: #fill next node
            new_node.next = self.head
            self.head = new_node
        else:
            while (temp.next != None) and (new_node.data.minDistance > temp.next.data.minDistance):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node


    def pop(self):
        if self.head == None:
            return None
        else:
            ret = self.head
            self.head = self.head.next
            return ret.data

    def remove(self, id):
        if id == self.head.data.id:
            self.pop()
        else:
            temp = self.head
            while temp.next.data.id != id:
                temp = temp.next
            toDelete = temp.next
            temp.next = toDelete.next


class Dijkstra:
    def __init__(self):
        self.vertexes = []

    def inQueue(self, vertexId, queue):
        temp = queue.head
        indicator = False

        while temp != None:
            if temp.data.id == vertexId:
                indicator = True
                return indicator
            temp = temp.next
        return indicator


    def computePath(self, sourceId):

        queue = PriorityQueue()

        for vertex in self.vertexes:
            if vertex.id == sourceId:
                vertex.minDistance = 0
            else:
                vertex.minDistance = np.inf
            vertex.previousVertex = None
            queue.push(vertex)

        while queue.head != None:
            vertex = queue.pop()
            for edge in vertex.edges:
                if self.inQueue(self.vertexes[edge.target].id, queue):
                    distance = edge.weight+vertex.minDistance
                    if self.vertexes[edge.target].minDistance > distance:
                        self.vertexes[edge.target].minDistance = distance
                        self.vertexes[edge.target].previousVertex = vertex.id
                        queue.remove(edge.target)
                        queue.push(self.vertexes[edge.target])

    def getShortestPathTo(self, targetId):
        path = []
        while self.vertexes[targetId].previousVertex != None:
            path.insert(0, self.vertexes[targetId])
            targetId = self.vertexes[targetId].previousVertex
        path.insert(0, self.vertexes[targetId])
        return path


    def createGraph(self, vertexes, edgesToVertexes):
        for vertex in vertexes:
            self.vertexes.insert(vertex.id, vertex) #add points

        for edge in edgesToVertexes:
            self.vertexes[edge.source].edges.append(edge) #add values

    def resetDijkstra(self):
        for vertex in self.vertexes:
            vertex.minDistance = np.inf
            vertex.previousVertex = None

    def getVertexes(self):
        return self.vertexes

