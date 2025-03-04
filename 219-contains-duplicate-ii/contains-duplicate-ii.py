
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, val in enumerate(nums):
            if val in seen and i - seen[val] <= k:
                return True
            else:
                seen[val] = i
        
        return False
# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         nums_set = set()        
#         for i in range(len(nums)):
#             if nums[i] in nums_set:
#                 return True
#             nums_set.add(nums[i])
#             if len(nums_set) > k:
#                 nums_set.remove(nums[i - k])
#         return False
