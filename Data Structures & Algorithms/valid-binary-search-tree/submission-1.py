# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def iterat(root,rang):
            if root.val > rang[0] and root.val < rang[1]:
                if root.left == None and root.right == None:
                    return True
                elif root.left == None:
                    return iterat(root.right,[root.val,rang[1]])
                elif root.right == None:
                    return iterat(root.left, [rang[0],root.val])
                else:
                    return iterat(root.right,[root.val,rang[1]]) and iterat(root.left, [rang[0],root.val])
            else:
                return False
        return iterat(root,[-float('inf'),float('inf')])