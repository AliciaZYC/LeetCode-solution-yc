from collections import defaultdict
from typing import List

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # 步骤1: 按x坐标分组，将相同x坐标的点的y值收集到一起
        # 例如: points = [[1,1],[1,3],[3,1],[3,3]] 
        # 会变成: {1: [1, 3], 3: [1, 3]}
        columns = defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        
        # 步骤2: 用字典记录每对(y1, y2)最后出现的x坐标
        # 键是(y1, y2)表示一条垂直边，值是该垂直边所在的x坐标
        lastx = {}
        
        # 初始化答案为无穷大
        ans = float('inf')
        
        # 步骤3: 按x坐标从小到大遍历每一列
        for x in sorted(columns):
            # 获取当前x坐标对应的所有y坐标，并排序
            # 排序是为了后续能按顺序遍历所有y对
            column = columns[x]
            column.sort()
            
            # 步骤4: 遍历当前列中所有可能的(y1, y2)对（垂直边）
            # j从0到len(column)-1，i从0到j-1，这样可以遍历所有组合
            for j, y2 in enumerate(column):
                for i in range(j):  # 注意：Python 3用range，不是xrange
                    y1 = column[i]
                    
                    # 步骤5: 检查之前是否出现过相同的垂直边(y1, y2)
                    # 如果出现过，说明可以形成矩形：
                    # - 之前的x坐标: lastx[(y1, y2)]
                    # - 当前的x坐标: x
                    # - 矩形宽度: x - lastx[(y1, y2)]
                    # - 矩形高度: y2 - y1
                    if (y1, y2) in lastx:
                        area = (x - lastx[(y1, y2)]) * (y2 - y1)
                        ans = min(ans, area)
                    
                    # 更新记录：将当前的(y1, y2)对对应的x坐标保存
                    lastx[(y1, y2)] = x
        
        # 步骤6: 如果找到了矩形，返回最小面积；否则返回0
        return ans if ans < float('inf') else 0