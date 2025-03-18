# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder = deque(preorder)

        # def build(preorder, inorder):
        #     if inorder:
        #         idx = inorder.index(preorder.popleft())
        #         root = TreeNode(inorder[idx])

        #         root.left = build(preorder, inorder[:idx])
        #         root.right = build(preorder, inorder[idx+1:])

        #         return root

        # return build(preorder, inorder)  
        inorder_map = {val: idx for idx, val in enumerate(inorder)}  # O(n) preprocessing
        pre_idx = 0  # Start from the first element in preorder
        
        def build(left, right):
            nonlocal pre_idx
            if left > right:
                return None
            
            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)
            
            inorder_root_idx = inorder_map[root_val]  # O(1) lookup
            
            # Build left subtree first (preorder processes left first)
            root.left = build(left, inorder_root_idx - 1)
            root.right = build(inorder_root_idx + 1, right)
            
            return root
        
        return build(0, len(inorder) - 1)