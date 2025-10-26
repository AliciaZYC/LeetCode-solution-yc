class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # pos=0
        # for i in range(0,len(nums)):
        #     if nums[i]==0:
        #         nums[pos],nums[i]=nums[i],nums[pos]
        #         pos+=1
        # for j in range(pos,len(nums)):
        #     if nums[j]==1:
        #         nums[pos],nums[j]=nums[j],nums[pos]
        #         pos+=1
        zeros, ones, n = 0, 0, len(nums)
        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
        for i in range(0, zeros):
            nums[i] = 0
        for i in range(zeros, zeros + ones):
            nums[i] = 1
        for i in range(zeros + ones, n):
            nums[i] = 2