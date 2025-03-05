class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points=sorted(points, key=lambda x: x[1])
        result=[points[0]]
        till=points[0][1]
        i=1
        while i<len(points):
            if points[i][0]>=till+1:
                result.append(points[i])
                till=points[i][1]
            i+=1
        return len(result)
