# '''
# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]
# '''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        outputList = [[1], [1,1]]
        for i in range(numRows-2):
            newList = [1]
            for j in range(len(outputList[-1])-1):
                newList.append(outputList[-1][j] + outputList[-1][j+1])
            newList.append(1)
            outputList.append(newList)
        return outputList


'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 
'''

class Solution2:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 1:
            return [1,1]
        outputList = [[1], [1,1]]
        for i in range(rowIndex-1):
            newList = [1]
            for j in range(len(outputList[-1])-1):
                newList.append(outputList[-1][j] + outputList[-1][j+1])
            newList.append(1)
            outputList.append(newList)
        return outputList[rowIndex]


