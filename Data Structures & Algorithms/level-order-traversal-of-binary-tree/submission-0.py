# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(n, depth):
            if not n:
                return []
            if len(res) == depth:
                res.append([])
            res[depth].append(n.val)
            dfs(n.left, depth + 1)
            dfs(n.right, depth + 1)

        dfs(root, 0)
        return res
            
      
        

        