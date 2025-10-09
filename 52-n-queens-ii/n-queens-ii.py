class Solution:
    def totalNQueens(self, n: int) -> int:
        # self.count 用于记录解决方案的总数
        self.count = 0
        # cols[i] 表示第 i 列是否已被占用
        cols = [False] * n
        # diag1 和 diag2 分别记录主对角线和副对角线是否被占用
        # 主对角线的特点是 row - col 的值相同，为了防止索引为负，加上 n
        # 副对角线的特点是 row + col 的值相同
        diag1 = [False] * (2 * n)
        diag2 = [False] * (2 * n)

        def backtrack(row: int):
            # 如果成功放置了 n 行，说明找到了一个有效的解决方案
            if row == n:
                self.count += 1
                return
            
            # 遍历当前行的每一列，尝试放置皇后
            for col in range(n):
                # 计算当前位置 (row, col) 对应的对角线索引
                d1 = row - col + n
                d2 = row + col
                
                # 如果当前列或对角线已被占用，则跳过
                if cols[col] or diag1[d1] or diag2[d2]:
                    continue
                
                # 放置皇后，并标记对应的列和对角线为已占用
                cols[col] = diag1[d1] = diag2[d2] = True
                
                # 递归到下一行
                backtrack(row + 1)
                
                # 回溯：撤销当前行的选择，以便尝试其他可能性
                cols[col] = diag1[d1] = diag2[d2] = False

        # 从第 0 行开始进行回溯搜索
        backtrack(0)
        return self.count