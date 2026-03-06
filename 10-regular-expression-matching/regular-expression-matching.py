class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # dp[i][j]：s 的前 i 个字符 与 p 的前 j 个字符是否匹配
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # 空串匹配空模式
        
        # 初始化：处理模式串以 * 开头的情况（题目保证 * 非首字符，但需处理如 "a*" 匹配空串）
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # * 匹配 0 次：忽略 * 及其前一个字符
                dp[0][j] = dp[0][j - 2]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.':
                    # '.' 匹配任意单个字符
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] != '*':
                    # 普通字符：需完全相等且前缀匹配
                    dp[i][j] = dp[i - 1][j - 1] and (p[j - 1] == s[i - 1])
                elif p[j - 2] != s[i - 1] and p[j - 2] != '.':
                    # '*' 前字符不匹配当前 s 字符 → 只能匹配 0 次
                    dp[i][j] = dp[i][j - 2]
                else:
                    # '*' 前字符匹配当前 s 字符（含 '.'）→ 三种可能：
                    # 1. dp[i][j-2]：匹配 0 次（跳过 * 及其前字符）
                    # 2. dp[i-1][j]：匹配 ≥1 次（消耗 s[i-1]，模式串保留 * 继续匹配）
                    # 3. dp[i][j-1]：匹配 1 次后模式串前进 1 位（* 被消耗，保留前字符）
                    # 注：标准解法通常仅需前两项（dp[i][j-2] 或 dp[i-1][j]），第三项在有效模式串下常冗余，
                    #     但本实现通过 LeetCode 全部测试用例，逻辑自洽。
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j] or dp[i][j - 2]
        
        return dp[m][n]  # 最终状态：完整字符串与完整模式串是否匹配