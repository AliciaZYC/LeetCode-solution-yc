# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        n = len(inorder)
        root_val = postorder[-1]
        root = TreeNode(root_val)
        if n==1:
            return root
        left_size = inorder.index(root_val)
        root.left = self.buildTree(inorder[:left_size], postorder[:left_size])
        root.right = self.buildTree(inorder[1+left_size:], postorder[left_size:-1])
        return root