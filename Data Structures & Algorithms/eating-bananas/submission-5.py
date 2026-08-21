class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            hours = 0
            m = l + (r - l) // 2
            for n in piles:
                hours += math.ceil(n / m)
            if hours > h:
                l = m + 1
            elif hours <= h:
                res = min(res, m)
                r = m - 1
        return res
    
        
        
            

        