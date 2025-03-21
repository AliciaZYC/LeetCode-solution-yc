# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.index = 0
        self.values = []
        self._inorder(root)

    def next(self) -> int:
        self.index +=1
        return self.values[self.index-1]

    def hasNext(self) -> bool:
        return self.index < len(self.values)
        
    def _inorder(self,root:TreeNode):
        if not root:
            return
        self._inorder(root.left)
        self.values.append(root.val)
        self._inorder(root.right)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()