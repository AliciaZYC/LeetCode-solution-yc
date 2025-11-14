class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSpilt(lim:int,nums,k):
            curr_sum = 0
            piece = 1
            for num in nums:
                if curr_sum + num > lim:
                    curr_sum = num
                    piece += 1

                    if piece > k:
                        return False
                else:
                    curr_sum += num
            return True
        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left)//2
            if canSpilt(mid,nums,k):
                right = mid
            else:
                left = mid + 1
        return left
