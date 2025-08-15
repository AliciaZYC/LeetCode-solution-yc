class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. 统计每个任务的频率
        freq = [0] * 26  # 26个字母
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        
        # 2. 排序，让频率最高的在最后
        freq.sort()
        
        # 3. 计算"块"的数量
        # chunk = 最高频率 - 1 = 完整间隔段的数量
        chunk = freq[25] - 1
        
        # 4. 计算总的空闲槽位
        # 每个间隔段需要n个槽位
        idle = chunk * n
        
        # 5. 用其他任务填充空闲槽位
        for i in range(24, -1, -1):
            # 每个任务最多能填充chunk个槽位
            idle -= min(chunk, freq[i])
        
        # 6. 返回结果
        # 如果还有空闲槽位，总时间 = 任务数 + 空闲槽位
        # 如果没有空闲槽位（idle < 0），说明任务很多，不需要空闲，总时间 = 任务数
        return len(tasks) + idle if idle >= 0 else len(tasks)