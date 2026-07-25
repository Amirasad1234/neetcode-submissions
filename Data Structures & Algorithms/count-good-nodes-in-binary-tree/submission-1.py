# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxVal = root.val
        count = 0
        def dfs(node, maxVal):
            nonlocal count
            if not node:
                return None
            if node.val < maxVal:
                dfs(node.right, maxVal)
                dfs(node.left, maxVal)
            else:
                maxVal = max(maxVal, node.val)
                count += 1
                dfs(node.right, maxVal)
                dfs(node.left, maxVal)
                return count 
        return dfs(root, maxVal)



        
    