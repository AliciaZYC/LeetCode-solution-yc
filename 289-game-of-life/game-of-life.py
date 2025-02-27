class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        temp = copy.deepcopy(board)
        for i in range(m):
            for j in range(n):
                ones = 0
                for x in range(max(0, i - 1), min(m, i + 2)):
                    for y in range(max(0, j - 1), min(n, j + 2)):
                        ones += temp[x][y]
                ones -= temp[i][j]
                if temp[i][j] == 1 and (ones <2 or ones >3):
                    board[i][j] =0
                elif temp[i][j] == 0 and ones == 3:
                    board[i][j] = 1
