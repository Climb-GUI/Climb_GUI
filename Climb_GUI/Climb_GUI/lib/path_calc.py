import math
import sys
from queue import Queue

def makeVertices(bounding_boxes):
    # bounding_boxes = [((x,y), (x,y)), ((x,y), (x,y)), ...]
    # vertices = [(((x,y), (x,y)), string,      int, graphnodes[x]), ...]
    # vertices = [(    value     ,  color, distance,   predecessor), ...]
    # bounding_boxes list of tuples with two tuples with x & y
    vertices = {}
    for node in bounding_boxes:
        vertices[node] = (node, "White", None, None)
        
    return vertices

def inRadius(curr, bounding_boxes):
    lis = []
    # iterating through bounding boxes, 
    # if distance between current and any box is close enough, add to list
    for box in bounding_boxes:
        if(dist(bounding_boxes[curr][1] - box[0]) < 100):
            lis.append(box)
    # lis = [((x,y), (x,y)), ((x,y), (x,y))]
    return lis
           
# distance formula
def dist(curr, next):     
    x = next[0] - curr[0]
    y = next[1] - curr[1]
    t1 = math.pow(x, 2)
    t2 = math.pow(y, 2)
    dist = math.sqrt(t1 + t2)
    
    return dist

def makeAdjList(bounding_boxes):
    # adj list should be index of node as key, 
    # then list of tuples after which are the connected nodes
    # map<key, set<tuple<tuple>>>
    # each key is assoc. with a set of tuples 
    # (bottom left corner of box and top right corner of box)
    # each item in the tuple is a coordinate, containing x & y coords of the point
    adjList = {}
    # adjlist = {
    #            key1: [((x,y), (x,y)), ((x,y), (x,y))]
    #            key2: [((x,y), (x,y)), ((x,y), (x,y))]
    #           }
    # iterating through bounding boxes, if key doesn't exist, add it
    # append the list for the specific key to map to the key
    # list for key contains tuple with two tuples
    
    for key in bounding_boxes:
        if(key not in adjList):
            adjList[key] = []
        adjList[key].append(inRadius(key, bounding_boxes))
    
    return adjList

# start is starting coordinates (current node)
def BFS(start, vertices, adjList):
    for vert in vertices:
        vert[0][1] = "White"
        vert[0][2] = sys.maxsize
        vert[0][3] = None

    vertices[start][1] = "Gray"
    vertices[start][2] = 0
    vertices[start][3] = None
    
    q = Queue()
    q.push((start, "White", -1, None))

    visited = list()

    while(not q.empty()):
        u = q.front()
        q.pop()
        visited.append(u[0])
        
        for adj in adjList[u[0]]:
            ad = vertices[adj]
            if(ad[1] == "White"):
                ad[1] = "Gray"
                ad[2] = u[2] + 1
                ad[3] = u[0]
                q.push(adj)

        u[1] = "Black"

    return visited

def shortestPath(start, end, vertices):
    BFS(start)

    pathLength = 0
    vertex = end

    while (vertex != start):
        v = vertices[vertex][3]
        vertex = v[0]
        pathLength = pathLength + 1

    return pathLength;      