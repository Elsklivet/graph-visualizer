import math
import sys

class Node:
    """Class to represent a graph vertex/node. Has an x and y coordinate.
    """
    def __init__(self, x: int, y: int):
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
        self.adj: list[list[Edge]] = [None] * self.v
        self.nodes: list[Node] = [None] * self.v
        self.marked: list[bool] = [False] * self.v
        self.edgeTo: list[Edge] = [None] * self.v
        self.distTo: list[float] = [sys.float_info.max] * self.v
        self.currPath: list[Edge] = []

    def __distance_formula(self,x1: float, y1: float, x2: float, y2: float):
        """Calculate the distance between two points using the distance formula.

        Args:
            x1 (float): first coordinate pair's x
            y1 (float): first coordinate pair's y
            x2 (float): second coordinate pair's x
            y2 (float): second coordinate pair's y

        Returns:
            float: distance between two points
        """
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    def __find_min(self, arr: list):
        """Return the index of the minimum item in an array. Used to bruteforce weighted searches without a priority queue.

        Args:
            arr (list(Edge)): Array to search for minimum edge in, based on weight

        Returns:
            int: index of minimum item in array
        """
        if not arr: return -1
        min = arr[0].weight
        index = 0
        for i in range(len(arr)):
            if arr[i].weight < min and not self.marked[arr[i].dest]:
                min = arr[i].weight
                index = i
                
        return index
    
    def __follow_path(self):
        pass
    
    def resetMarked(self):
        self.marked = [False] * self.v
        
    def resetEdgeTo(self):
        self.edgeTo = [-1] * self.v
        
    def resetCurrPath(self):
        self.currPath = []
    
    def resetDistTo(self):
        self.distTo = [sys.float_info.max] * self.v

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
            
            
    def BFS (self, source):
        """Run BFS on the graph from a start node.

        Args:
            source (int): index of starting node to run BFS on
        """
        queue: list[int] = []
        self.marked[source] = True
        queue.append(source)
        while queue:
            _from: int = queue.pop(0)
            for edge in self.adj[_from]:
                node = edge.dest
                if not self.marked[node]:
                    self.currPath.append(edge)
                    self.edgeTo[node] = edge
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
                self.edgeTo[node] = edge
                self.DFS(node)
    
    def weightedDFS (self, source):
        """Run DFS on the graph from a start node, preferring min weighted edges.

        Args:
            source (int): index of starting node to run wDFS on
        """
        self.marked[source] = True
        edge = self.adj[source][self.__find_min(self.adj[source])]
        node = edge.dest
        if not self.marked[node]:
            self.currPath.append(edge)
            self.edgeTo[node] = source
            self.weightedDFS(node)
        # TODO: unfinished
            
    def dijkstrasDict(self, source):
        """Dijkstra's algorithm using a sorted dictionary as a pseudo Priority Queue.

        Args:
            source (int): index of starting node
        """
        # Just a sorted dictionary tbh, acts like an indexable PQ
        pq: dict[int,float] = {}
        # Set source distance to 0
        self.distTo[source] = 0
        self.marked[source] = True
        # Pseudo Priority Queue
        pq[source] = 0
        # Index structure
        indices: list[int] = []
        while pq:
            # Re sort our "priority queue"
            indices = sorted(pq, key=pq.__getitem__)
            # Get the current node by grabbing the first index from the priority queue,
            # since this is guaranteed to be the minimum weighted edge source.
            curr: int = indices[0]
            # delete from pq
            pq.pop(indices.pop(0))
            # Iterate over outbound edges from this source
            for i in range(len(self.adj[curr])):
                # Get edge and edge's destination
                edge = self.adj[curr][i]
                to = edge.dest
                # If the distance added by this edge is less than the current distance,
                # then this is the new best edge to this destination.
                if self.distTo[curr] + edge.weight < self.distTo[to]:
                    # Set destinations distance array to this new distance.
                    self.distTo[to] = self.distTo[curr] + edge.weight
                    # Set the edge to this destination to this edge.
                    self.edgeTo[to] = edge
                    # Add this distance to the priority queue.
                    pq[to] = self.distTo[to]
                    
        # Now build a path out of this
        for edge in self.edgeTo:
            if edge:
                self.marked[edge.dest] = True
                self.currPath.append(edge)
                
    def dijkstrasDictDest(self, source, destination):
        """Dijkstra's algorithm using a sorted dictionary as a pseudo Priority Queue.

        Args:
            source (int): index of starting node
            destination (int): index of destination node
        """
        # Just a sorted dictionary tbh, acts like an indexable PQ
        pq: dict[int,float] = {}
        # Set source distance to 0
        self.distTo[source] = 0
        self.marked[source] = True
        # Pseudo Priority Queue
        pq[source] = 0
        # Index structure
        indices: list[int] = []
        while pq:
            # Re sort our "priority queue"
            indices = sorted(pq, key=pq.__getitem__)
            # Get the current node by grabbing the first index from the priority queue,
            # since this is guaranteed to be the minimum weighted edge source.
            curr: int = indices[0]
            # delete from pq
            pq.pop(indices.pop(0))
            # Iterate over outbound edges from this source
            for i in range(len(self.adj[curr])):
                # Get edge and edge's destination
                edge = self.adj[curr][i]
                to = edge.dest
                # If the distance added by this edge is less than the current distance,
                # then this is the new best edge to this destination.
                if self.distTo[curr] + edge.weight < self.distTo[to]:
                    # Set destinations distance array to this new distance.
                    self.distTo[to] = self.distTo[curr] + edge.weight
                    # Set the edge to this destination to this edge.
                    self.edgeTo[to] = edge
                    # Add this distance to the priority queue.
                    pq[to] = self.distTo[to]
                    
        # Now build a path out of this.
        # This will work differently than default dijkstra's because we only care about the 
        # paths that go to the destination node.
        
        edge = self.edgeTo[destination]
        stack = []
        while edge:
            self.marked[edge.dest] = True
            stack.append(edge)
            edge = self.edgeTo[edge.src]
        
        while stack:
            self.currPath.append(stack.pop())
            
        

def loadFromFile(filename: str = "savefile.txt"):
    """Load a graph from a save file.

    Args:
        filename (str): File path to read from
        
    Returns:
        (Graph): Graph object created from loading process
    """
    lines = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        # First line is number of nodes
        v = int(lines[0])
        # Initialize graph object of appropriate size
        G = Graph(v)
        # Iterate over the first 'v' lines after line 1, which will be the nodes.
        for i in range(1,v+1):
            line = lines[i]
            data = line.split(',')
            index = int(data[0])
            x = int(data[1])
            y = int(data[2])
            G.addNode(x,y,index)
        
        # The remainder of the file are the edges.
        for i in range(v+1, len(lines)):
            line = lines[i]
            data = line.split(',')
            _from = int(data[0])
            to = int(data[1])
            # weight unused, get rid of this later
            weight = float(data[2])
            G.addEdge(_from, to)
    
        return G
        
        
            

def saveToFile(G: Graph, filename: str = "savefile.txt"):
    """Save a graph to a given file.
    
    Args:
        G (Graph): Graph object to save
        filename (str): File path to save to
    """
    
    
    with open(filename, 'w') as file:
        # Need to write out the number of nodes as first line.
        file.write(str(G.v))
        file.write("\n")
        # Next need to write out every node
        # index,x,y
        index = 0
        for node in G.nodes:
            line = f"{str(index)},{str(node.x)},{str(node.y)}\n"
            file.write(line)
            index = index + 1
        
        assert G.v == len(G.nodes)
        
        # Finally must write out all edges
        # from_index,to_index,weight
        for i in range(len(G.nodes)):
            for edge in G.adj[i]:
                line = f"{str(edge.src)},{str(edge.dest)},{str(edge.weight)}\n"
                file.write(line)
