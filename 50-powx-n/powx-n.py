class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1

        # 正/负数次方
        if n < 0:
            flag = -1
        else:
            flag = 1
        n = abs(n)

        # 例如 3**4 = 9**2 = 81**1 =》 ans = 81
        while n != 0:
            if n%2 == 0:   #even
                x = x*x
                n = n//2
            else:
                ans = ans*x
                n = n-1

        if flag == -1:
            return 1/ans
        return ans
