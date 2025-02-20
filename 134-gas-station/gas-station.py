class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_diff = 0
        current_diff = 0
        start_index = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_diff += diff
            current_diff += diff

            if current_diff < 0:
                current_diff = 0
                start_index = i + 1

        return start_index if total_diff >= 0 else -1