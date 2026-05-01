class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = sum(s * s for _, _, s in squares)
        target = total_area / 2

        def area_below(y):
            """所有正方形在 y 以下的面积之和"""
            res = 0.0
            for x, yi, s in squares:
                top = yi + s
                if y <= yi:
                    res += 0
                elif y >= top:
                    res += s * s
                else:
                    res += (y - yi) * s  # 部分覆盖
            return res

        # 二分 y 的范围
        lo = min(sq[1] for sq in squares)
        hi = max(sq[1] + sq[2] for sq in squares)

        for _ in range(50):  # 100次足够精度
            mid = (lo + hi) / 2
            if area_below(mid) < target:
                lo = mid
            else:
                hi = mid

        return (lo + hi) / 2