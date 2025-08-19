class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # 1. between 2 persons
        # 2. to the left or right
        res, dist = 0, seats.index(1)
        
        for seat in seats:
            if seat: 
                res, dist = max(res, math.ceil(dist/2)), 0
            else: 
                dist += 1
                
        return max(res, dist)
            