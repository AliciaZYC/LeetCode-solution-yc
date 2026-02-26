class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right
        while left < right:
            mid = left + (right - left)//2
            hours = 0
            for pile in piles:
                hours += (pile+mid-1)//mid #向上取整
            if hours <= h:
                ans = mid
                right = mid
            else:
                left = mid + 1
        return ans

        