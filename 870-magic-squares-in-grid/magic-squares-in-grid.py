class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans = 0
        m,n = len(grid),len(grid[0])
        for row in range(m-2):
            for col in range(n-2):
                if self._isMagicSqure(grid,row,col):
                    ans += 1
        return ans
    def _isMagicSqure(self,grid,row,col):
        sequence = "2943816729438167"
        sequenceReversed = "7618349276183492"
        border = []
        borderIndices = [0,1,2,5,8,7,6,3]
        for i in borderIndices:
            num = grid[row + i//3][col + (i%3)]
            border.append(str(num))
        borderConverted = "".join(border)
        return (
            grid[row][col] %2 == 0
            and (
                sequence.find(borderConverted) != -1
                or sequenceReversed.find(borderConverted) != -1
            )
            and grid[row + 1][col + 1] ==5
        )