# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: index for index, val in enumerate(inorder)}
        '''
        {
            2: 0
            1: 1
            3: 2
            4: 3
        }

        p : [1, 2, 3, 4]
        '''
        counter = 0
        def dfs(l, r):
            nonlocal counter
            if l > r:
                return None
            
            rootVal = preorder[counter]
            root = TreeNode(rootVal)
            counter += 1
            mid = indices[rootVal]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root


        
        return dfs(0, len(preorder) - 1) # dfs(0, 3)
