# Graph Algorithm Visualizer

In preparation for the final exam for my CS1501 course at the University of Pittsburgh, I was reading my *Algorithms* textbook (Sedgewick and Wayne) and saw some pretty cool visuals depicting the process of running graph algorithms. I thought, "wow, it would be cool to make a program that animates the process of these graph algorithms running," and that's what I intend to do in this repo.

## Algorithms

Right now, the algorithms that are implemented are:

* **Breadth First Search (BFS)**: Breadth first search searches level-by-level in a graph, not moving on to a new level until it has searched all of a node's neighbors.
* **Depth First Search (DFS)**: Depth first search searches as far down one path as it can go until it reaches a dead end, then backtracks and attempts to do so again.
* **Dijkstra's**: Dijkstra's algorithm finds the minimum-weighted path from a source node to all nodes (makes an MST) or to a specific destination node.
    - *with priority queue and no destination*: Using a "priority queue" (actually just a sorted dictionary), the minimum distance at each step is set to the current best edge.
    - *with priority queue and a destination*: Using a "priority queue", the minimum distance edge is taken at each step and only the path to the destination is shown.

In the future, I hope to add:
* **Prim's**: An algorithm for making a minimum spanning tree (MST) of the graph.
    - *Lazy*: Using a PQ of all crossing edges, pick minimum weighted edge at each step.
    - *Eager*: Using a PQ of only the minimum edges to *non-tree* vertices, pick minimum weighted tree->non-tree edge at each step. (Similar to dijsktra's under the hood).
* **Kruskal's**: Another algorithm for making a minimum spanning tree, but this one does not only go from tree->non-tree, instead it creates multiple connected components at once and eventually connects them. At each step, the minimum weighted edge that does not create a cycle is added.
    - *with weighted-tree, path compressed union-find*: Using a union-find structure, cycles can be detected more efficiently.

## Sources Cited
The algorithms in this repo were not invented by me, and much of the inspiration for their implementations came from various sources. While there are only so many ways to code a specific algorithm anyway, I got specific ideas from the following sources:

Sedgewick, Robert, and Kevin Wayne. *Algorithms*. 4th edition, Addison-Wesley, 2011.
