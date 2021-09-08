#importing queue for BFS
import queue
from operator import itemgetter

#Undirected graph
class Graph:
    class Node:
        def __init__(self, data):
            self.data = data
            #each item in self.neighbours is a list with two items [neighbour_node, weight]
            self.neighbours = []
        

    def __init__(self, v = 0):
        #number of vertices
        self.v  = 0
        #adjacency list
        self.nodes = {}

    #adds an edge between node1, and node2
    def add_edge(self, node1, node2, weight = 0):
        node1.neighbours.append([node2,weight])
        node2.neighbours.append([node1,weight])
        if node1 not in self.nodes:
            self.v += 1
            self.nodes[node1] = node1.neighbours
        if node2 not in self.nodes:
            self.v += 1 
            self.nodes[node2] = node2.neighbours
    
    #deletes edge between node1 and node2
    def remove_edge(self, node1, node2, weight):
        node1.neighbours.remove([node2,weight])
        node2.neighbours.remove([node1, weight])

    #TODO: remove nodes 

    def print_graph(self):
        for key in self.nodes:
            print(key.data, " : " ,end =" ")
            for neighbour in self.nodes[key]:
                print([neighbour[0].data, neighbour[1]],end = " ")
            print("\n")

    def dfs(self, starting_node, visited = set()):
        if starting_node not in visited:
            visited.add(starting_node)
            print(starting_node.data)
            for children in self.nodes[starting_node]:
                self.dfs(children[0],visited)

    def bfs(self, starting_node):
        node_queue = queue.Queue()
        visited = set()

        node_queue.put(starting_node)
        visited.add(starting_node)

        while not node_queue.empty():
            node_exploring_now = node_queue.get()
            print(node_exploring_now.data)
            visited.add(node_exploring_now)
            for neighbour in node_exploring_now.neighbours:
                if neighbour[0] not in visited:
                    node_queue.put(neighbour[0])

    def detect_cycle_bfs(self):
        node_queue = queue.Queue()
        visited_nodes = {}

        for node in self.nodes:
            visited_nodes[node] = -1

        for node in self.nodes:
            node_queue.put(node)
            visited_nodes[node] = 0
            break
        
       
        while not node_queue.empty():
            visited_node = node_queue.get()
            visited_nodes[visited_node] = 1
            for each_neighbour in visited_node.neighbours:
                if visited_nodes[each_neighbour[0]] == 0:
                    return True
                elif visited_nodes[each_neighbour[0]] != 1:
                    node_queue.put(each_neighbour[0])
                    visited_nodes[each_neighbour[0]] = 0
        return False
                    
    
    def detect_cycle_dfs(self, parent, starting_node, visited, unvisited):
        if starting_node in visited:
            return True
        else:
            visited.add(starting_node)
            unvisited.remove(starting_node)
            for child in starting_node.neighbours:
                if child[0] != parent:
                    cycle = self.detect_cycle_dfs(starting_node, child[0], visited, unvisited)
                    if cycle is True:
                        return True
            return False

    def detect_cycle(self):
        visited_nodes = set()
        unvisited_nodes = set()
        for node in self.nodes:
            unvisited_nodes.add(node)

        for node in self.nodes:
            starting_node = node
            break
        
        return self.detect_cycle_dfs(starting_node, starting_node, visited_nodes, unvisited_nodes)

    def prims_algorithm(self):
        edges = []
        visited = set()
        unvisited = set()
        for each_node in self.nodes:
            unvisited.add(each_node)
        
        #randomly choses a node to be added to visited as a starting node
        for node in self.nodes:
            visited.add(node)
            unvisited.remove(node)
            break

        #Actual Prim's algorithm
        while len(unvisited) > 0:
            minimum_distance = float('inf')
            next_node = None
            next_edge = None
            for node in visited:
                for each_neighbour in node.neighbours:
                    if each_neighbour[0] not in visited and each_neighbour[1] < minimum_distance:
                        minimum_distance = each_neighbour[1]
                        next_node = each_neighbour[0]
                        next_edge = (node, each_neighbour[0])
            unvisited.remove(next_node)
            visited.add(next_node)
            edges.append(next_edge)
        tuple_representation = []
        for edge in edges:
            tuple_representation.append((edge[0].data, edge[1].data))
        return tuple_representation


    # def kruskals_algorithm(self):
    #     new_tree = Graph()
    #     new_tree.v = self.v
    #     new_tree.nodes = {}
    #     unsorted_edges = []


    #     for node in self.nodes:
    #         for neighbour in self.nodes[node]:
    #             if not ([neighbour[0], node, neighbour[1]] in unsorted_edges)cle:
    #                 edge = [node, neighbour[0], neighbour[1]]
    #                 unsorted_edges.append(edge)
        
        
    #     sorted_edges = sorted(unsorted_edges, key=itemgetter(2))
    #     sorted_edges.reverse()

    #     for i in range(-1, -len(sorted_edges),-1):
    #         print(sorted_edges[i][0].data, sorted_edges[i][1].data, sorted_edges[i][2])
        #     new_tree.add_edge(sorted_edges[i][0], sorted_edges[i][1], sorted_edges[i][2])
        #     new_tree.print_graph()
        #     print(sorted_edges[i][0].data, sorted_edges[i][1].data, sorted_edges[i][2])
        #     if new_tree.detect_cycle():
        #         new_tree.remove_edge(sorted_edges[i][0], sorted_edges[i][1], sorted_edges[i][2])

        # tuple_representation = []
        # for node in new_tree.nodes:
        #     for neighbour in node.neighbours:
        #         tuple_representation.append([node.data, neighbour.data])

        # return tuple_representation
    
    def djikstra(self, source_node):
        #if node is not in unvisited, it means it has been visited and does not need to be explored
        unvisited = set()
        #parent of where each node comes from
        parent = {}
        #distance so far
        distance = {}
        for node in self.nodes:
            print(type(node))
            unvisited.add(node)
            distance[node] = float("inf")
            parent[node] = None

        distance[source_node] = 0
        current_node = source_node
        parent[source_node] = source_node

        while len(unvisited) > 0:
            for neighbour in current_node.neighbours:
                if neighbour[0] in unvisited:
                    if distance[neighbour[0]] > distance[current_node] + neighbour[1]:
                        distance[neighbour[0]] = distance[current_node] + neighbour[1]
                        parent[neighbour[0]] = current_node
            
            unvisited.remove(current_node)
            minimum_distance = float('inf')
            for node in unvisited:
                if distance[node] < minimum_distance:
                    minimum_distance = distance[node]
                    current_node = node

        better_dict = {}
        for key in parent:
            better_dict[key.data] = parent[key].data

        return better_dict

a = Graph.Node("a")
b = Graph.Node("b")
c = Graph.Node("c")
d = Graph.Node("d")
e = Graph.Node("e")
f = Graph.Node("f")
g = Graph.Node("g")
graph = Graph()        
graph.add_edge(a,b,2)
graph.add_edge(a,d,7)
graph.add_edge(a,f,5)
graph.add_edge(a,c,4)
graph.add_edge(b,d,6)
graph.add_edge(b,g,8)
graph.add_edge(b,e,3)
graph.add_edge(c,f,6)
graph.add_edge(d,f,1)
graph.add_edge(d,g,6)
graph.add_edge(e,g,7)
graph.add_edge(f,g,6)

print(graph.djikstra(a))

        


        