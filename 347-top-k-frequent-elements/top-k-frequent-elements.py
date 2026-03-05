import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 步骤1：统计每个数字的出现频率（O(n)）
        counter = Counter(nums)
        
        # 步骤2：维护大小为k的最小堆（堆顶 = 当前k个元素中频率最小的）
        heap = []
        for num, freq in counter.items():
            # 将(频率, 数字)入堆（heapq默认最小堆，按频率排序）
            heapq.heappush(heap, (freq, num))
            # 堆大小超过k时，弹出频率最小的元素（淘汰机制）
            if len(heap) > k:
                heapq.heappop(heap)
        
        # 步骤3：提取堆中所有数字（顺序任意，题目允许）
        # 注意：堆中元素顺序不保证频率降序，但题目要求"任意顺序"即可
        return [num for freq, num in heap]