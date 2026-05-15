class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        # 辅助函数：计算排序后 bars 中最长连续递增1的序列长度（即连续被移除的栅栏数量）
        def maxLen(bars: List[int]) -> int:
            # 初始化：至少需2个连续栅栏才能形成有效空隙段，故初始计数为2
            count = length = 2
            # 遍历排序后的栅栏位置
            for i in range(1, len(bars)):
                if bars[i] - bars[i-1] == 1:  # 当前栅栏与前一个连续
                    count += 1
                else:
                    count = 2  # 不连续则重置计数
                length = max(length, count)   # 更新最长连续段长度
            return length
        
        # 分别对水平/垂直栅栏排序，便于检测连续段
        hBars.sort()
        vBars.sort()
        
        # 关键提示：问题中“空隙长度 = 连续移除栅栏数 + 1”
        # 当前代码直接使用连续栅栏数作为边长，建议思考此处逻辑是否需调整
        side = min(maxLen(hBars), maxLen(vBars))
        return side * side