class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        low = d[0] + d[1]
        high = 2 * low * 2
        ans = high
        lcm = (r[0] *r[1])//math.gcd(r[0],r[1])
        def can_complete(time):
            slots1 = time - (time//r[0])
            slots2 = time - (time//r[1])
            total_slots = time - (time//lcm)
            return (slots1 >= d[0]) and (slots2 >= d[1]) and (total_slots >= d[0]+d[1])
        while low <= high:
            mid = (low + high)//2
            if can_complete(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans