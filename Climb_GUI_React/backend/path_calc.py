import sys
from collections import deque

from scipy.spatial import KDTree


class Vertex:
    def __init__(self, value):
        self.value = value
        self.color = "White"
        self.distance = sys.maxsize
        self.predecessor = None


def makeVertices(bounding_boxes):
    """
    Create vertices for all bounding boxes.
    """
    return {node: Vertex(node) for node in bounding_boxes}


def buildAdjList(bounding_boxes, radius):
    """
    Build an adjacency list using a KDTree for efficient nearest neighbor search.
    """
    centers = [
        ((box[0][0] + box[1][0]) / 2, (box[0][1] + box[1][1]) / 2)
        for box in bounding_boxes
    ]
    tree = KDTree(centers)

    adjList = {}
    for idx, center in enumerate(centers):
        indices = tree.query_ball_point(center, r=radius)
        adjList[bounding_boxes[idx]] = [bounding_boxes[i] for i in indices if i != idx]

    return adjList


def bfsShortestPath(start, end, vertices, adjList):
    """
    Perform BFS to find the shortest path from start to end.
    """
    # Initialize BFS
    for vert in vertices.values():
        vert.color = "White"
        vert.distance = sys.maxsize
        vert.predecessor = None

    vertices[start].color = "Gray"
    vertices[start].distance = 0
    vertices[start].predecessor = None

    queue = deque([start])
    while queue:
        u = queue.popleft()

        for neighbor in adjList.get(u, []):
            if vertices[neighbor].color == "White":
                vertices[neighbor].color = "Gray"
                vertices[neighbor].distance = vertices[u].distance + 1
                vertices[neighbor].predecessor = u
                queue.append(neighbor)

                # Early exit if we reached the end
                if neighbor == end:
                    break

        vertices[u].color = "Black"

    # Reconstruct the path
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = vertices[current].predecessor

    return path if path[0] == start else None


def shortestPath(start, end, bounding_boxes, radius):
    """
    Find the shortest path between start and end using BFS.
    """
    try:
        vertices = makeVertices(bounding_boxes)
        adjList = buildAdjList(bounding_boxes, radius)
        return bfsShortestPath(start, end, vertices, adjList)
    except Exception as e:
        print(f"Error in shortestPath: {e}")
        return None
