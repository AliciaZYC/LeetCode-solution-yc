# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = root.left
        r = root.right
        h1,h2 = 0,0
        while l is not None:
            l=l.left
            h1+=1
        while r is not None:
            r=r.right
            h2+=1
        if h1==h2:
            return 2**(h1+1)-1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)