# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root):
        checkifValidBst = self.inOrderTraversal(root)
        print(checkifValidBst)
        for i in range(len(checkifValidBst)-1):
            if checkifValidBst[i+1] < checkifValidBst[i]:
                return False
        return True
        
        
        
    def inOrderTraversal(self, root, outputList = []):
        if root is None:
            return outputList
        if root.left is not None:
            self.inOrderTraversal(root.left, outputList)
        outputList.append(root.val)
        if root.right is not None:
            self.inOrderTraversal(root.right, outputList)
        return outputList

root = TreeNode(0)
solution = Solution()
print(solution.isValidBST(root))