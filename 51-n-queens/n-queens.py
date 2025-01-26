class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Initialize the board and result list
        board = [['.'] * n for _ in range(n)]
        res = []
        # Call the backtrack function starting from the first row
        self.backtrack(board, 0, n, res)
        return res

    def backtrack(self, board: List[List[str]], row: int, n: int, res: List[List[str]]):
        # If all rows are filled, add the current board configuration to results
        if row == n:
            res.append(["".join(row) for row in board])
            return
        
        # Try placing a queen in each column of the current row
        for col in range(n):
            if self.is_safe(board, row, col, n):
                # Place the queen
                board[row][col] = 'Q'
                # Recursively backtrack to the next row
                self.backtrack(board, row + 1, n, res)
                # Remove the queen (backtrack)
                board[row][col] = '.'

    def is_safe(self, board: List[List[str]], row: int, col: int, n: int) -> bool:
        # Check column for other queens
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check the top-left diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # Check the top-right diagonal
        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True