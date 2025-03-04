
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hset = {}
        for idx in range(len(nums)):
            if nums[idx] in hset and abs(idx - hset[nums[idx]]) <= k:
                return True
            hset[nums[idx]] = idx
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
