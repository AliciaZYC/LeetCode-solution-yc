class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 1
        window_max, window_min = deque(), deque()
        left = 0
        s = 0
        for right in range(n):
            while window_max and nums[window_max[-1]] <= nums[right]:
                window_max.pop()
            while window_min and nums[window_min[-1]] >= nums[right]:
                window_min.pop()
            window_max.append(right)
            window_min.append(right)

            while nums[window_max[0]] - nums[window_min[0]] > k:
                if window_max[0] == left:
                    window_max.popleft()
                if window_min[0] == left:
                    window_min.popleft()
                s = (s - dp[left]) % MOD
                left += 1
            
            s = (s + dp[right]) % MOD
            dp[right + 1] = s
        
        return dp[n]