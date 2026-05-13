class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        # 计算 1 到 n 的原始总和 S
        S = n * (n + 1) // 2
        # 可行性校验：
        # 1. (S + target) 必须为偶数（等价于 (S - target) 为偶数，确保可构造子集和）
        # 2. |target| 不能超过 S（总和调整范围限制）
        if (S + target) % 2 or abs(target) > S:
            return []
        
        L, R = [], []  # L: 存放取反后的负数（按处理顺序）；R: 存放保持正数的数字（按处理顺序）
        # 从大到小遍历数字（贪心核心）：优先决策大数符号，以控制字典序
        for a in range(n, 0, -1):
            # 剩余数字 (1 到 a-1) 的最大可调整范围（全为正时的和）
            remaining_max = a * (a - 1) // 2
            # 决策逻辑：
            # 若将 a 取反（贡献 -a），剩余需达成的目标变为 target + a
            # 若 target + a ≤ remaining_max，说明剩余数字有能力“补偿”该目标（可行性保证下界自动满足）
            if target + a <= remaining_max:
                L.append(-a)  # 选择取反：负数放入 L（保证后续字典序更小）
                target += a    # 更新剩余目标：因 a 贡献 -a，需由更小数字多补偿 a
            else:
                R.append(a)    # 保持正数：放入 R
                target -= a    # 更新剩余目标：a 贡献 +a，需由更小数字少补偿 a
        
        # 拼接结果：
        # L 中负数按“绝对值从大到小”排列 → 数值升序（如 [-5, -3]），字典序更小
        # R 原为降序（如 [4, 2, 1]），反转后为升序（[1, 2, 4]），使正数部分字典序最小
        return L + R[::-1]