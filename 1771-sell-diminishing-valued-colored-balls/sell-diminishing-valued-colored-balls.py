# class Solution:
#     def maxProfit(self, inventory: List[int], orders: int) -> int:
#         left, right = 0, max(inventory)
#         while left < right:
#             mid = left + (right - left + 1) // 2
#             cnt = 0
#             for num in inventory:
#                 if num > mid:
#                     cnt += num - mid
#             if cnt >= orders:
#                 left = mid
#             else:
#                 right = mid - 1
#         t = left
#         total = 0
#         sold = 0
#         for ball in inventory:
#             if ball > t:
#                 cnt = ball - t
#                 total += (ball + t + 1) * cnt //2
#                 sold += cnt
#         extra = sold - orders
#         res = total - extra * (t + 1)
#         return res % (10**9+7) 

from collections import Counter
from typing import List

class Solution:
    def maxProfit(self, inv: List[int], orders: int) -> int:
        MOD = 1_000_000_007

        cnt = Counter(inv)
        vals = sorted(cnt, reverse=True)
        vals.append(0)

        ans = 0
        width = 0

        for i in range(0, len(vals) - 1):
            v = vals[i]

            width += cnt[v]
            next_v = vals[i + 1]
            sell = min(orders, width * (v - next_v))
            whole, rem = divmod(sell, width)

            ans += width * (whole * (2 * v - whole + 1)) // 2
            ans += rem * (v - whole)

            orders -= sell
            if orders == 0:
                break

        return ans % MOD