# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def height(node):
            if not node:
                return 0
            leftdepth= height(node.left)
            rightdepth= height(node.right)

            if abs(leftdepth-rightdepth)>=2:
                self.balanced = False
            return 1 + max(leftdepth, rightdepth)
        height(root)
        return self.balanced

        
        