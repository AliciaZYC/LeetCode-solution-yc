class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area, max_y = 0, 0

        for x, y, l in squares:
            total_area += l**2
            max_y = max(max_y, y+l)
        
        def area_below(y_limit):
            area = 0
            for x, y, l in squares:
                if y < y_limit:
                    area += l * min(l, y_limit - y)
            
            return area

        left, right = float(min(y for x, y, l in squares)), float(max_y)
        eps = 10**-5
        while right-left > eps:
            mid = left+(right-left)/2

            if area_below(mid) >= total_area / 2:
                right = mid
            
            else:
                left = mid
        
        return right