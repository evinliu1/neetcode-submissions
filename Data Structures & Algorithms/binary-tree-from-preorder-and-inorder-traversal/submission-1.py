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
            9: 0
            '3: 1'
            15: 2
            20: 3
            7: 4
        } in order

         '0'  1  2   3   4
        [3, 9, 20, 15, 7] preorder
        '''
        prefix = 0

        def dfs(l, r):
            nonlocal prefix
            if l > r:
                return None

            rootVal = preorder[prefix]
            prefix += 1
            root = TreeNode(rootVal)
            mid = indices[rootVal]

            root.left = dfs(l, mid - 1)

            root.right = dfs(mid + 1, r)
            return root
        
        return dfs(0, len(preorder) - 1) # dfs(0, 4)


