'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      return sorted(nums, reverse=True)[k-1]
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        priority_queue = []
        for num in nums:
            heapq.heappush(priority_queue,num)
            if len(priority_queue)>k:
                heapq.heappop(priority_queue)
        return priority_queue[0]