# Import the required libraries
from tkinter import *
from tkinter import ttk
from random import *
import time
import math

from graph import Graph
from graph import Node
from graph import Edge
from graph import saveToFile
from graph import loadFromFile

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
        
        # Animation delay
        self.step_delay = 500

        # Number of nodes
        self.V = 16
        # Graph init
        self.G = Graph(self.V)

        # Generate nodes
        for i in range(self.V):
            self.G.addNode(randint(10,690), randint(10,690), i) 

        # Generate edges
        for i in range(self.V):
            self.G.addEdge(randint(0,self.V-1), randint(0,self.V-1))
        
        # self.G = loadFromFile("savefile.txt")
        
        self.drawalledges()
                
        self.drawnodes()
        
        # Generate source nodes and destination nodes
        src = randint(0, self.G.v-1)
        dest = randint(0, self.G.v-1)
        
        self.drawnode(src,"green",1)
        self.drawnode(dest,"red",1)
                
        self.G.dijkstrasDictDest(src, dest)
        
        self.drawpathedges()
        
        self.drawmarkednodes("cyan")
        
        # Show the start and end of the dijkstra's path in green and red
        self.drawnode(src,"green",1)
        self.drawnode(dest,"red",1)
        
        self.G.resetCurrPath()
        self.G.resetMarked()
        self.G.resetEdgeTo()
    
    def drawalledges(self, color="gray", w=2):
        for adjlist in self.G.adj:
            for edge in adjlist:
                src = self.G.nodes[edge.src]
                dest = self.G.nodes[edge.dest]
                # print(edge.weight)
                self.linedraw(src.x, src.y, dest.x, dest.y, color, w)       
                
    def drawpathedges(self, color="tomato", w=2):
        for edge in self.G.currPath:
            src = self.G.nodes[edge.src]
            dest = self.G.nodes[edge.dest]
            self.canvas.after(self.step_delay, self.linedraw(src.x, src.y, dest.x, dest.y, color, w))
            self.canvas.update()
            
    def drawnode(self, index=0, color="white", w=1):
        node = self.G.nodes[index]
        self.canvas.create_oval(node.x-4, node.y-4, node.x+4, node.y+4, fill=color, width=w)
        
    def drawnodes(self, color="white", w=1):
        for node in self.G.nodes:
            self.canvas.create_oval(node.x-4, node.y-4, node.x+4, node.y+4, fill=color, width=w)
            
    def drawmarkednodes(self, color="cyan", w=1):
        i = 0
        for node in self.G.nodes:
            if self.G.marked[i]:
                self.canvas.create_oval(node.x-4, node.y-4, node.x+4, node.y+4, fill=color, width=w)
            i = i + 1

    def linedraw(self,x1,y1,x2,y2,fillcolor,w=2):
        self.canvas.create_line(x1,y1,x2,y2,fill=fillcolor,width=w)


if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()
    # Saving and loading is not fully supported yet, but the save operations do work.
    # saveToFile(gui.G, "savefile.txt")