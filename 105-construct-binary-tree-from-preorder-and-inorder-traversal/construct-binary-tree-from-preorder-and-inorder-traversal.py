class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)} 
        pre_idx = 0 
        def build(left, right):
            nonlocal pre_idx
            if left > right:
                return None
            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)
            inorder_root_idx = inorder_map[root_val]  
            # Build left subtree first (preorder processes left first)
            root.left = build(left, inorder_root_idx - 1)
            root.right = build(inorder_root_idx + 1, right)
            return root
        
        return build(0, len(inorder) - 1)