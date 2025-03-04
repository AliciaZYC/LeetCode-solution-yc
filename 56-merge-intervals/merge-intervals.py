class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sort_re=sorted(intervals, key=lambda x: x[0])
        for i in range(1,len(intervals)):
          if sort_re[i][0]<=sort_re[i-1][1]:
            sort_re[i]=[sort_re[i-1][0],max(sort_re[i-1][1],sort_re[i][1])]
            sort_re[i-1]=0
          i+=1
        re = [item for item in sort_re if item != 0]
        return re
