class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmin, curmax = 1, 1
        for n in nums:
            if n == 0:
                curmin, curmax = 1, 1
                continue
            tpm = curmin * n
            curmin = min(curmin * n, curmax * n, n)
            curmax = max(tpm, curmax * n, n)
            res = max(curmax, res)
        return res
       

            

            

        