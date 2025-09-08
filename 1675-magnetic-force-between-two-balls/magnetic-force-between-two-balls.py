class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        ans = 0
        n = len(position)
        position.sort()
        low = 1
        high = int(position[-1]/(m-1.0))+1
        while low <= high:
            mid = low + (high-low)//2
            if self.can_place(mid,position,m):
                ans = mid
                low = mid + 1
            else:
                high = mid -1
        return ans
    def can_place(self, x, position, m):
        prev_ball_pos = position[0]
        balls_placed = 1
        for i in range(1, len(position)):
            cur_pos = position[i]
            if cur_pos - prev_ball_pos >= x:
                balls_placed += 1
                prev_ball_pos = cur_pos
            if balls_placed == m:
                return True
        return False

    