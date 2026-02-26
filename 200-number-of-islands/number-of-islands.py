class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 边界处理：空网格直接返回0
        if not grid:
            return 0
        
        # 深度优先搜索：从坐标(i,j)出发，将相连的陆地全部标记为"0"（淹没岛屿）
        def dfs(i, j):
            # 终止条件：越界 或 遇到水域（"0"）或已访问位置
            if (i < 0 or i >= len(grid) or 
                j < 0 or j >= len(grid[0]) or 
                grid[i][j] != "1"):
                return
            
            # 标记当前陆地为已访问（原地标记，避免额外空间）
            grid[i][j] = "0"
            
            # 递归探索四个方向：上、下、左、右
            dfs(i - 1, j)  # 上
            dfs(i + 1, j)  # 下
            dfs(i, j - 1)  # 左
            dfs(i, j + 1)  # 右
        
        num_of_island = 0  # 岛屿计数器
        
        # 遍历整个网格
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 发现新陆地（"1"），说明找到新岛屿
                if grid[i][j] == "1":
                    num_of_island += 1
                    dfs(i, j)  # 淹没整个岛屿，避免重复计数
        
        return num_of_island