# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        x = []
        def rod(root,level,x):
            if root is None:
                return 
            if len(x) <= level :
                x.append([])
            x[level].append(root.val)
            rod(root.left,level+1,x)
            rod(root.right,level+1,x)
            return x
        rod(root,0,x)
        return x