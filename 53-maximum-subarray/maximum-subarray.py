class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        plus=0
        for num in nums:
            if plus <0:
                plus=0
            plus+=num
            res=max(res,plus)
        return res