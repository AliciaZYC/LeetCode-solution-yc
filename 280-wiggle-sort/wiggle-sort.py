class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        i = 1
        while i < len(nums)-1:
            nums[i],nums[i+1]=nums[i+1],nums[i]
            i+=2

# class Solution:
#     def wiggleSort(self, nums: List[int]) -> None:
#         for i in range(1, len(nums)):
#             if i % 2 == 1:  # 应该是波峰：nums[i] >= nums[i-1]
#                 if nums[i] < nums[i-1]:
#                     nums[i], nums[i-1] = nums[i-1], nums[i]
#             else:           # 应该是波谷：nums[i] <= nums[i-1]
#                 if nums[i] > nums[i-1]:
#                     nums[i], nums[i-1] = nums[i-1], nums[i]