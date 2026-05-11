class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.row = [0] * n
        self.col = [0] * n
        self.dia = [0] * 2

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.row[row] += 1
            self.col[col] += 1
            if row == col:
                self.dia[0] += 1
            if row + col == self.n - 1:
                self.dia[1] += 1
            if self.row[row] == self.n or self.col[col] == self.n or self.dia[0] == self.n or self.dia[1] == self.n:
                return 1
        else:
            self.row[row] -= 1
            self.col[col] -=1
            if row == col:
                self.dia[0] -=1
            if row + col == self.n - 1:
                self.dia[1] -= 1
            if self.row[row] == -self.n or self.col[col] == -self.n or self.dia[0] == -self.n or self.dia[1] == -self.n:
                return 2
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)