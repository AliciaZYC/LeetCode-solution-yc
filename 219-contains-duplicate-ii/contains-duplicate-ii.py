
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i,val in enumerate(nums):
            if i>k:
                seen.remove(nums[i-k-1])
            if val in seen:
                return True
            seen.add(val)
            
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
