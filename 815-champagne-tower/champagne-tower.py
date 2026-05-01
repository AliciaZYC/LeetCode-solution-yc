class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # tower[i][j] 表示流入第i行第j个杯子的总量
        tower = [[0.0] * (query_row + 2) for _ in range(query_row + 2)]
        tower[0][0] = poured

        for i in range(query_row):
            for j in range(i + 1):
                overflow = tower[i][j] - 1.0
                if overflow > 0:
                    tower[i+1][j]   += overflow / 2
                    tower[i+1][j+1] += overflow / 2
        
        return min(1.0, tower[query_row][query_glass])