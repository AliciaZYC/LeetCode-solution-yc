class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 构建有向图：adjList[i] 表示课程 i 的后续课程（i → 后续课程）
        # 边方向：c2 → c1 表示 "学 c1 需先学 c2"
        adjList = [[] for _ in range(numCourses)]
        for c1, c2 in prerequisites:
            adjList[c2].append(c1)
        
        visited = set()  # 全局记录：所有已访问过的节点（避免重复遍历）
        
        def hasCycle(v: int, stack: list) -> bool:
            """
            DFS检测环：stack维护当前递归路径（用于检测回边）
            返回True表示发现环（不可完成）
            """
            if v in visited:
                # 若节点已在全局访问集：
                # - 在当前路径stack中 → 发现回边（环）
                # - 不在当前路径 → 该分支已验证无环，安全跳过
                return v in stack
            
            visited.add(v)
            stack.append(v)  # 将当前节点加入递归路径
            
            for neighbor in adjList[v]:
                if hasCycle(neighbor, stack):
                    return True  # 递归中发现环，立即终止
            
            stack.pop()  # 回溯：移出当前路径
            return False
        
        # 遍历所有课程节点（处理非连通图）
        for v in range(numCourses):
            # 优化：若节点已访问，可跳过（当前实现由hasCycle内部处理）
            if hasCycle(v, []):
                return False  # 发现环 → 无法完成所有课程
        
        return True  # 无环 → 可完成