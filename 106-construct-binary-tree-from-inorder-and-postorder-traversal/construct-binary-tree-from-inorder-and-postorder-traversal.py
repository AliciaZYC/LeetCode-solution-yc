# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        # if not inorder:
        #     return None
        # n = len(inorder)
        # root_val = postorder[-1]
        # root = TreeNode(root_val)
        # if n==1:
        #     return root
        # left_size = inorder.index(root_val)
        # root.left = self.buildTree(inorder[:left_size], postorder[:left_size])
        # root.right = self.buildTree(inorder[1+left_size:], postorder[left_size:-1])
        # return root
        inorder_map = {val: idx for idx, val in enumerate(inorder)}  # O(n) preprocessing
        post_idx = len(postorder) - 1  # Start from the last element of postorder
        
        def build(left, right):
            nonlocal post_idx
            if left > right:
                return None
            
            root_val = postorder[post_idx]
            post_idx -= 1
            root = TreeNode(root_val)
            
            inorder_root_idx = inorder_map[root_val]  # O(1) lookup
            
            # Build right subtree first because postorder processes right last
            root.right = build(inorder_root_idx + 1, right)
            root.left = build(left, inorder_root_idx - 1)
            
            return root
        
        return build(0, len(inorder) - 1)