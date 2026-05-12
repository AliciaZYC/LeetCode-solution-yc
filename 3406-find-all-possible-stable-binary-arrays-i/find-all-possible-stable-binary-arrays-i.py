class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10 ** 9 + 7  # 大数取模，防止整数溢出
        L = limit + 1      # 连续相同字符的最大允许长度 + 1，用于滑动窗口边界判断

        # dp0[i][j]: 使用 i 个 '0' 和 j 个 '1' 构成的稳定数组中，以 '0' 结尾的方案数
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        # dp1[i][j]: 使用 i 个 '0' 和 j 个 '1' 构成的稳定数组中，以 '1' 结尾的方案数
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]

        # 初始化：仅含 '0' 的情况（无 '1'）
        # 当连续 '0' 的数量 ≤ limit 时，只有一种排列（全0），否则无法构成稳定数组（此处循环已限定范围）
        for i in range(1, min(zero, limit) + 1):
            dp0[i][0] = 1  # i 个 0 且以 0 结尾，仅当 i ≤ limit 时有效
        
        # 初始化：仅含 '1' 的情况（无 '0'）
        for j in range(1, min(one, limit) + 1):
            dp1[0][j] = 1  # j 个 1 且以 1 结尾，仅当 j ≤ limit 时有效

        # 动态规划填表：枚举使用的 0 和 1 的数量
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # 计算以 '0' 结尾的方案数：
                # 1. 从 (i-1, j) 状态转移：前一个字符是 '0'（dp0[i-1][j]）或 '1'（dp1[i-1][j]）
                # 2. 减去非法情况：若当前添加 '0' 后导致末尾连续 '0' 超过 limit，
                #    即前 L 个字符（含当前）全为 '0'，需减去 (i-L, j) 位置以 '1' 结尾的方案数（dp1[i-L][j]）
                #    （当 i < L 时无需减，因不可能超限）
                subtract0 = dp1[i - L][j] if i >= L else 0
                dp0[i][j] = (dp0[i - 1][j] + dp1[i - 1][j] - subtract0) % MOD

                # 计算以 '1' 结尾的方案数（逻辑对称）：
                # 减去 (i, j-L) 位置以 '0' 结尾的方案数，避免末尾连续 '1' 超限
                subtract1 = dp0[i][j - L] if j >= L else 0
                dp1[i][j] = (dp0[i][j - 1] + dp1[i][j - 1] - subtract1) % MOD

        # 最终结果：所有使用 zero 个 '0' 和 one 个 '1' 的稳定数组方案数（以 '0' 或 '1' 结尾之和）
        return (dp0[zero][one] + dp1[zero][one]) % MOD