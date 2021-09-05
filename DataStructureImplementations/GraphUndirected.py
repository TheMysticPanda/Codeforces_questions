#Undirected graph
class Graph:
    class Node:
        def __init__(self, data):
            self.data = data
            #each item in self.neighbours is a list with two items [name_of_neighbour_node, weight]
            self.neighbours = []

    def __init__(self, v = 0):
        #number of vertices
        self.v  = 0
        #adjacency list
        self.nodes = {}

    def add_edge(self, node1, node2, weight = 0):
        node1.neighbours.append([node2,weight])
        node2.neighbours.append([node1,weight])
        if node1 not in self.nodes:
            self.v += 1
            self.nodes[node1] = node1.neighbours
        if node2 not in self.nodes:
            self.v += 1 
            self.nodes[node2] = node2.neighbours
    

    def print_graph(self):
        for key in self.nodes:
            print(key.data, " : " ,end =" ")
            for neighbour in self.nodes[key]:
                print([neighbour[0].data, neighbour[1]],end = " ")
            print("\n")

    def dfs(self):

    def bfs(self):

    


a = Graph.Node("a")
b = Graph.Node("b")
c = Graph.Node("c")
d = Graph.Node("d")
e = Graph.Node("e")
graph = Graph()        
graph.add_edge(a,b,5)
graph.add_edge(b,e,4)
graph.add_edge(a,d,3)
graph.add_edge(c,e,9)
graph.print_graph()

        


        