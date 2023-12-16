import math
import sys
from queue import Queue

class Vertex:
    def __init__(self, value):
        self.value = value
        self.color = "White"
        self.distance = -1
        self.predecessor = None

def makeVertices(bounding_boxes):
    # bounding_boxes = [((x,y), (x,y)), ((x,y), (x,y)), ...]
    # vertices = [(((x,y), (x,y)),  color, distance,   predecessor), ...]
    vertices = {}
    for node in bounding_boxes:
        vertices[node] = Vertex(node)
        
    return vertices

def BFS(start, vertices, adjList):
    for vert in vertices.values():
        vert.color = "White"
        vert.distance = sys.maxsize
        vert.predecessor = None

    vertices[start].color = "Gray"
    vertices[start].distance = 0
    vertices[start].predecessor = None

    q = Queue()
    q.put(start)

    visited = []

    while not q.empty():
        u = q.get()
        visited.append(u)

        for adj in adjList[u]:
            ad = vertices[adj]
            if ad.color == "White":
                ad.color = "Gray"
                ad.distance = vertices[u].distance + 1
                ad.predecessor = vertices[u]
                q.put(adj)

        vertices[u].color = "Black"

    return visited

def inRadius(curr, bounding_boxes, vertices, radius):
    lis = []
    for i in range(len(bounding_boxes)):
        # 100 is hard coded value, change to something else
        if dist(vertices[curr].value[1], bounding_boxes[i][0]) < radius:
            lis.append(bounding_boxes[i])
    return lis

def dist(curr, next):     
    x = next[0] - curr[0]
    y = next[1] - curr[1]
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

def makeAdjList(bounding_boxes, vertices, radius):
    # adjlist = {
    #            key1: [((x,y), (x,y)), ((x,y), (x,y))]
    #            key2: [((x,y), (x,y)), ((x,y), (x,y))]
    #           }
    adjList = {}
    for key in bounding_boxes:
        adjList[key] = []
        adjList[key].extend(inRadius(key, bounding_boxes, vertices, radius))
    return adjList

def shortestPath(start, end, bounding_boxes, radius):
    vertices = makeVertices(bounding_boxes)
    adjList = makeAdjList(bounding_boxes, vertices, radius)
    BFS(start, vertices, adjList)

    path = []
    current_vertex = end

    while current_vertex != start:
        path.insert(0, current_vertex)
        current_vertex = vertices[current_vertex].predecessor.value

    path.insert(0, start)
    return path