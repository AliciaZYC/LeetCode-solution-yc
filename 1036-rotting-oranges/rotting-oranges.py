class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(i,j,minute):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or (grid[i][j] > 1 and grid[i][j] < minute):
                return
            grid[i][j] = minute
            dfs(i + 1, j, minute + 1)
            dfs(i - 1, j, minute + 1)
            dfs(i, j + 1, minute + 1)
            dfs(i, j - 1, minute + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    dfs(i, j, 2)
        minutes = 2
        for row in grid:
            for cell in row:
                if cell == 1:
                    return -1
                minutes = max(minutes, cell)
        return minutes - 2