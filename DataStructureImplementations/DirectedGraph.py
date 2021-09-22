class DirectedGraph:
    def __init__(self):
        self.n = 0
        self.nodes = {}
        self.nodeSet = set()

    def addEdge(self, here, there):
        if here in self.nodes:
            self.nodes[here].append(there)
        else:
            self.nodes[here] = [there]
        if there not in self.nodes:
            self.nodes[there] = []
        if here not in self.nodeSet:
            self.nodeSet.add(here)
        if there not in self.nodeSet:
            self.nodeSet.add(there)
      

    def detectCycle(self):
        unvisited = self.nodeSet
        gray = set()
        black = set()
        while len(unvisited) != 0:
            for node in self.nodes:
                if node not in black:
                    cycleDetect, unvisited, gray, black = self.detectCycleHelper(node, unvisited, gray, black)
                    if cycleDetect == True:
                        return True
        return False
            


    def detectCycleHelper(self, node, unvisited, gray, black):
        if node in black:
            return 
        unvisited.remove(node)
        gray.add(node)
        print(unvisited, gray, black)
        for neighbour in self.nodes[node]:
            if neighbour in unvisited:
                self.detectCycleHelper(neighbour, unvisited, gray, black)
            elif neighbour in gray:
                return (True, unvisited, gray, black) 
        gray.remove(node)
        black.add(node)
        print("returnValue", gray, black)
        return (False, unvisited, gray, black)

       
            
        
graph = DirectedGraph()
graph.addEdge(1,2)
graph.addEdge(2,3)
graph.addEdge(1,3)
graph.addEdge(4,1)
graph.addEdge(4,5)
graph.addEdge(5,6)
graph.addEdge(6,4)
print(graph.detectCycle())