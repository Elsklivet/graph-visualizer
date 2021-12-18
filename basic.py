# Import the required libraries
from tkinter import *
from tkinter import ttk
from random import *
import time
import math

from graph import Graph
from graph import Node
from graph import Edge

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

        self.V = 25

        self.G = Graph(self.V)

        for i in range(self.V):
            self.G.addNode(randint(10,690), randint(10,690), i) 

        
        for i in range(self.V**2):
            self.G.addEdge(randint(0,self.V-1), randint(0,self.V-1))
        
        for adjlist in self.G.adj:
            for edge in adjlist:
                src = self.G.nodes[edge.src]
                dest = self.G.nodes[edge.dest]
                # print(edge.weight)
                color = "gray"
                self.linedraw(src.x, src.y, dest.x, dest.y, color)
                
        self.G.BFS(0)
        for edge in self.G.currPath:
            src = self.G.nodes[edge.src]
            dest = self.G.nodes[edge.dest]
            # print(edge.weight)
            color = "tomato"
            self.linedraw(src.x, src.y, dest.x, dest.y, color, 2)
        
        
                
        for node in self.G.nodes:
            self.canvas.create_oval(node.x-4, node.y-4, node.x+4, node.y+4, fill="white", width=1)


    def linedraw(self,x1,y1,x2,y2,fillcolor,w=2):
        self.canvas.create_line(x1,y1,x2,y2,fill=fillcolor,width=w)


if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()