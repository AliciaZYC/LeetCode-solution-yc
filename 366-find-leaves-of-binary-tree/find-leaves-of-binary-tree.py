# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 初始化结果列表，每层叶子节点值存为一个子列表
        res = []

        # DFS函数：剥离当前层所有叶子节点，并返回更新后的子树根
        def DFS(node):
            # 空节点直接返回None
            if not node:
                return None
            # 当前节点为叶子节点（无左右子节点）
            if not (node.left or node.right):
                # 将叶子值加入最新创建的层（res最后一项）
                res[-1].append(node.val)
                # 返回None，使父节点断开与此节点的连接（逻辑删除）
                return None
            # 递归处理左子树，并更新左指针（可能被置为None）
            node.left = DFS(node.left)
            # 递归处理右子树，并更新右指针
            node.right = DFS(node.right)
            # 非叶子节点保留，返回自身供上层连接
            return node

        # 循环剥离：每轮处理一层叶子，直到树为空
        while root:
            # 为当前层新建空列表
            res.append([])
            # 执行剥离，更新root（若整棵树已清空则root=None）
            root = DFS(root)
        # 返回按剥离顺序组织的叶子层列表
        return res