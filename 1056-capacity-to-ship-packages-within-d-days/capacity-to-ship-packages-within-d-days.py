class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left,right = max(weights),sum(weights)
        while left < right:
            mid = left + (right - left)//2
            daysNeed, currWeight = 1,0
            for weight in weights:
                if currWeight + weight > mid:
                    daysNeed += 1
                    currWeight = 0
                currWeight += weight
            if daysNeed > days:
                left = mid + 1
            else: 
                right = mid
        return left