# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        def isIdentical(s,t):
            if s == None and t == None:
                return True
            if s and t and s.val == t.val:
                return isIdentical(s.left,t.left) and isIdentical(s.right,t.right)
            return False
        if isIdentical(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
