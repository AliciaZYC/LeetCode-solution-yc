class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 按照开始时间排序
        intervals.sort(key=lambda x: x[0])
        # 初始化结果列表，放入第一个区间
        merged = [intervals[0]]
        # 从第二个区间开始遍历
        for i in range(1, len(intervals)):
            # 获取结果列表中最后一个区间
            last_interval = merged[-1]
            current_interval = intervals[i]
            # 如果当前区间的开始时间 <= 最后一个区间的结束时间，则合并
            if current_interval[0] <= last_interval[1]:
                # 更新最后一个区间的结束时间为两个区间结束时间的最大值
                merged[-1][1] = max(last_interval[1], current_interval[1])
            else:
                # 如果不重叠，直接添加当前区间
                merged.append(current_interval)
        return merged

