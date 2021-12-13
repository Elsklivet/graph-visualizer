# Import the required libraries
from tkinter import *
from tkinter import ttk
from random import *
import time
import math

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def tupleify(self):
        return (x,y)

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

class Graph:
    """
    Class to represent an undirected graph with a specified number of nodes.
    """
    def __init__(self, numNodes):
        self.v = numNodes
        self.adj = [None] * self.v
        self.nodes = [None] * self.v

    def __distance_formula(x1,y1,x2,y2):
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)

    def addNode(self,x,y,index):
        """
        Add a node to the graph at index 'index' and with specified x and y.
        """
        n = Node(x,y)
        if self.nodes[index] == None:
            self.nodes[index] = n
            self.adj[index] = [n]
            return True
        else: return False
    
    def addEdge(self, n1, n2):
        """
        Add an edge (and a corresponding backedge) between nodes at index 'n1' and 'n2'.
        """
        if self.adj[n1] != None:
            self.adj[n1].append(n2)
        if self.adj[n2] != None:
            self.adj[n2].append(n1)

    def collectNear(self, n, num):
        """
        Collect the closest 'num' nodes to node 'n' (n is an index).
        """
        # Get x and y coordinates of node at given index.
        x,y = self.nodes[n].x, self.nodes[n].y

        # Init a list of the nearest 'num' nodes.
        near_nodes = [None] * num
        # Distance array, defaulting to a big number that is unlikely to 
        # be a real distance.
        distances = [4096] * self.v

        # Correct num if it's too large.
        if num > self.v: num = self.v

        # Iterate over reach node in the graph
        for i in range(self.v):
            # If the current node is not the node we were given
            if i != n:
                # Grab the coordinates of this node
                nx,ny = self.nodes[i].x,self.nodes[i].y
                # Calculate the distance between these two points
                dist = __distance_formula(x,y,nx,ny)
                # Associate this distance with the node.
                # The `i`th entry in the distance array corresponds
                # to the distance from node `n` to the `i`th node in
                # the graph.
                distances[i] = dist
        
        # Have an array of the distances from this node to every other node
        # Now need to get the lowest 'num' values of this array WITHOUT
        # changing their physical positions, because their positions associate them
        # to their corresponding nodes. Then, need to add the nodes at these 
        # indexes to the near_nodes array and return.
        


class GUI(Tk):
    def __init__(self):
        super().__init__()

        self.title("Graph Visualizations")
        self.geometry("700x700")
        self['bg']="black"

        self.style = ttk.Style(self)
        self.style.configure(
            'TLabel',
            background='black',
            foreground='white')

        self.canvas = Canvas(self, width=700, height=700)
        self.canvas.configure(bg="black", bd=0)
        self.canvas.pack()

        self.V = 250

        self.G = Graph(self.V)

        for i in range(self.V):
            self.G.addNode(randint(10,690), randint(10,690), i) 

        for node in self.G.nodes:
            self.canvas.create_oval(node.x-2, node.y-2, node.x+2, node.y+2, fill="white", width=1)
            # We're going to calculate the nearest ten nodes from this node and
            # add edges from this node to each of those nodes (and vice versa)
            # so the graph is not too dense.


        self.prims()

    def linedraw(self,x1,y1,x2,y2,fillcolor):
        self.canvas.create_line(x1,y1,x2,y2,fill=fillcolor,width=5)

    def prims(self):
        pass

if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()