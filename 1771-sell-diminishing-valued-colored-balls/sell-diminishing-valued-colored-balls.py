class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        left, right = 0, max(inventory)
        while left < right:
            mid = left + (right - left + 1) // 2
            cnt = 0
            for num in inventory:
                if num > mid:
                    cnt += num - mid
            if cnt >= orders:
                left = mid
            else:
                right = mid - 1
        t = left
        total = 0
        sold = 0
        for ball in inventory:
            if ball > t:
                cnt = ball - t
                total += (ball + t + 1) * cnt //2
                sold += cnt
        extra = sold - orders
        res = total - extra * (t + 1)
        return res % (10**9+7) 