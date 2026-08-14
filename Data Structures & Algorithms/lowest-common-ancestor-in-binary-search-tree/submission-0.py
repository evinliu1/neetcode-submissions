# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(node, p, q):
            if not node:
                return
            
            if node == p or node == q:
                return node
            
            l = dfs(node.left, p, q)
            r = dfs(node.right, p, q)

            if l and r:
                return node
            else:
                return l or r


        return dfs(root, p, q)