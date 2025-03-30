class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def num_to_pos(num):
            r = n - 1 - (num - 1) // n
            c = (num - 1) % n
            if (n - r) % 2 == 0:
                c = n - 1 - c
            return r, c

        visited = set()
        queue = deque()
        queue.append((1, 0))  # (当前编号, 步数)

        while queue:
            curr, steps = queue.popleft()
            for move in range(1, 7):
                next_num = curr + move
                if next_num > n * n:
                    continue
                r, c = num_to_pos(next_num)
                if board[r][c] != -1:
                    next_num = board[r][c]
                if next_num == n * n:
                    return steps + 1
                if next_num not in visited:
                    visited.add(next_num)
                    queue.append((next_num, steps + 1))
        return -1
