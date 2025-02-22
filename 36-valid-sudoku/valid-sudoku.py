class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                # if is number
                if element != '.':
                    # row, column and the 3*3 box
                    # types (int, str), (str, int), (int, int, str)
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))