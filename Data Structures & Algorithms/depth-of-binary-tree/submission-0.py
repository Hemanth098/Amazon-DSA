# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        def depth(root):
            if root.right == None and root.left == None:
                return 1
            elif root.right == None:
                return 1 + depth(root.left)
            elif root.left == None:
                return 1 + depth(root.right)
            return max(1+depth(root.left),1+depth(root.right))
        return depth(root)