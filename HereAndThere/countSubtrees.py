class Solution:
    def countSubTrees(self, n: int, edges, labels: str):
        nodes = {}
        solved = []
        for i in range(n):
            nodes[i] = []
            solved.append(None) 

        for edge in edges:
            nodes[edge[0]].append(edge[1])
        
        for node in nodes:
            if len(nodes[node]) == 0:
                solved[node] = 1 

        for node in nodes:
            if solved[node] == None:
                answer = self.helper(node, nodes, solved, labels)
                return answer



    def helper(self, node, nodes, solved, labels):
            if solved[node] == None:
                count = 1
                for children in nodes[node]:
                    #call the function on its children
                    tempCount = self.helper(children, nodes, solved, labels)
                    if labels[node] == labels[children]:
                        count += tempCount[children]
                solved[node] = count 
                return solved
            else:
                return solved


solution = Solution()
# solution.countSubTrees(7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],"abaedcd")
# print("-------------------------------")
# solution.countSubTrees(4,[[0,1],[1,2],[0,3]],"bbbb" )
# print("-------------------------------")
solution.countSubTrees(5, [[0,1],[0,2],[1,3],[0,4]], "aabab")
# print("-------------------------------")
# solution.countSubTrees(6, [[0,1],[0,2],[1,3],[3,4],[4,5]], "cbabaa")
# print("-------------------------------")
# solution.countSubTrees(7, [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]], "aaabaaa")