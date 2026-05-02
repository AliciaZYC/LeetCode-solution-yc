class Solution:
    def maxOperations(self, s: str) -> int:
        # "maximum" 策略是数1，当1的右侧有0，就加上1的累积个数
        cnt = 0
        ans = 0
        i = 0
        while i < len(s):
            if s[i] == "0":
                while i + 1 < len(s) and s[i + 1] == "0":
                    i += 1
                ans += cnt
            else:
                cnt += 1
            i += 1
        return ans