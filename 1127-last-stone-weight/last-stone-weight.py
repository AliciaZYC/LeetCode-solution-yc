class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heap.append(-stone)
        heapify(heap)
        while len(heap)>1:
            s1 = heappop(heap)
            s2 = heappop(heap)
            if s1 != s2:
                heappush(heap,s1-s2)
        if heap:
            return -heap[0]
        return 0