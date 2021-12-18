import math

class Node:
    """Class to represent a graph vertex/node. Has an x and y coordinate.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def tupleify(self):
        return (self.x,self.y)

    def __eq__(self, other):
        if other is self:
            return True
        elif isinstance(other,Node):
            return other.x == self.x and other.y == self.y
        else:
            return False

    def __ne__(self, other):
        if other is self:
            return False
        elif isinstance(other, Node):
            return other.x != self.x or other.y != self.y
        else:
            return False
        
class Edge:
    """Class to represent a directed, weighted edge.
    """
    def __init__(self, source, destination, weight):
        self.src = source
        self.dest = destination
        self.weight = weight
        
    def tupleify(self):
        return (self.src, self.dest, self.weight)
    
class Graph:
    """
    Class to represent an undirected graph with a specified number of nodes.
    Undirection is represented by using two edges, i.e. A<->B == A->B and B->A.
    """
    def __init__(self, numNodes=32):
        self.v = numNodes
        self.adj: list(Edge) = [None] * self.v
        self.nodes: list(Node) = [None] * self.v
        self.marked: list(bool) = [False] * self.v
        self.edgeTo: list(int) = [-1] * self.v
        self.currPath: list(Edge) = []

    def __distance_formula(self,x1,y1,x2,y2):
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    def resetMarked(self):
        self.marked = [False] * self.v
        
    def resetEdgeTo(self):
        self.edgeTo = [-1] * self.v
        
    def resetCurrPath(self):
        self.currPath = []

    def addNode(self,x,y,index):
        """
        Add a node to the graph at index 'index' and with specified x and y.
        """
        n = Node(x,y)
        if self.nodes[index] == None:
            self.nodes[index] = n
            self.adj[index] = []
            return True
        else: return False
    
    def addEdge(self, n1, n2):
        """
        Add an edge (and a corresponding backedge) between nodes at index 'n1' and 'n2'.
        """
        if n1 == n2: return
        node1 = self.nodes[n1]
        node2 = self.nodes[n2]
        distance = self.__distance_formula(node1.x, node1.y, node2.x, node2.y)

        if self.adj[n1] != None:
            self.adj[n1].append(Edge(n1, n2, distance))
        if self.adj[n2] != None:
            self.adj[n2].append(Edge(n2, n1, distance))
            
            
    def BFS(self, source):
        """Run BFS on the graph from a start node.

        Args:
            source (int): index of starting node to run BFS on
        """
        queue: list(int) = []
        self.marked[source] = True
        queue.append(source)
        while queue:
            _from: int = queue.pop(0)
            for edge in self.adj[_from]:
                node = edge.dest
                if not self.marked[node]:
                    self.currPath.append(edge)
                    self.edgeTo[node] = _from
                    self.marked[node] = True
                    queue.append(node)
                    
    def DFS (self, source):
        """Run DFS on the graph from a start node.

        Args:
            source (int): index of starting node to run DFS on
        """
        self.marked[source] = True
        for edge in self.adj[source]:
            node = edge.dest
            if not self.marked[node]:
                self.currPath.append(edge)
                self.edgeTo[node] = source
                self.DFS(node)
        

def loadFromFile(filename: str) -> Graph:
    """Load a graph in from a given file.
    """
    pass

def saveToFile(G: Graph, filename: str) -> None:
    """Save a graph to a given file.
    """
    pass