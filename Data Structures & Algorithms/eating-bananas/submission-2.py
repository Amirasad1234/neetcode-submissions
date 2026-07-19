class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            m = l + (r - l) // 2
            Totaltime = 0
            for p in piles:
                Totaltime += math.ceil(p / m)
            if Totaltime <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res


        