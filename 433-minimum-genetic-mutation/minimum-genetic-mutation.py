class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # 将 bank 转成 set，提升查找效率，同时方便删除
        bank = set(bank)
        # 初始化队列，存储元组：(当前基因序列，变化步数)
        dq = deque([(startGene, 0)])

        # 开始 BFS 遍历
        while dq:
            curr_gene, steps = dq.popleft()  # 取出当前基因序列和已变异次数
            # 如果当前基因就是目标基因，返回当前步数
            if curr_gene == endGene:
                return steps
            # 枚举当前基因的每一位字符
            for i, ch in enumerate(curr_gene):
                # 尝试将这一位变成其他三种字符（A、C、G、T）
                for new_ch in "ACGT":
                    if new_ch != ch:  # 跳过和原字符相同的变换
                        # 构造变异后的新基因序列
                        mutated = curr_gene[:i] + new_ch + curr_gene[i+1:]

                        # 如果这个新序列在 bank 里（即合法变异）
                        if mutated in bank:
                            bank.remove(mutated)  # 标记访问过，避免重复走
                            dq.append((mutated, steps + 1))  # 入队，步数+1

        # 如果遍历完也没找到目标序列，返回 -1
        return -1
