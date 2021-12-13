# Import the required libraries
from tkinter import *
from tkinter import ttk
from random import *
import time
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def tupleify(self):
        return (x,y)

class Graph:
    def __init__(self, numNodes):
        self.v = numNodes
        self.adj = [None] * self.v
        self.nodes = list()

    def addNode(self,x,y):
        n = Node(x,y)
        self.nodes.append(n)
        self.adj[self.nodes.index(n)] = []
        return True
    
    def addEdge(self, n1, n2):
        if self.adj[n1] != None:
            self.adj[n1].append(n2)
            return True
        else: return False


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

        self.canvas = Canvas()

        G = Graph(32)

        for i in range(32):
            G.addNode(randint(20,680), randint(20,680))

        for i in range(32):
            G.addEdge(i, randint(0,31))

        i=0
        for edge in G.adj:
            self.linedraw(G.nodes[i].x, G.nodes[i].y, G.nodes[edge[0]].x, G.nodes[edge[0]].y, "white")

        self.prims()

    def linedraw(self,x1,y1,x2,y2,fillcolor):
        self.canvas.create_line(x1,y1,x2,y2,fill=fillcolor,width=5)

    def prims(self):
        pass

if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()