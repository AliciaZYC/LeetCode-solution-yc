class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # left = 0
        # right = len(nums)-1
        # while left < right:
        #     mid = left + (right - left)//2
        #     if nums[mid] > nums[mid+1]:
        #         right = mid
        #     else:
        #         left = mid+1
        # return left
        n = len(nums)
        if n == 1:
            return 0
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                return i-1
        return n-1