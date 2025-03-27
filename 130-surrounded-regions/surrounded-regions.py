class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        self.rows = len(board)
        self.cols = len(board[0])

        from itertools import product
        borders = list(product(range(self.rows), [0, self.cols - 1])) + list(
            product([0, self.rows - 1], range(self.cols))
        )
        for row,col in borders:
            self.dfs(board, row, col)

        for r in range(self.rows):
            for c in range(self.cols):
                if board[r][c] == "O":
                    board[r][c] = "X"  # captured
                elif board[r][c] == "E":
                    board[r][c] = "O"  # escaped

    def dfs(self, board, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return 
        if board[row][col]!="O":
            return
        board[row][col] = "E"
        for ro,co in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            self.dfs(board, row+ro, col+co)