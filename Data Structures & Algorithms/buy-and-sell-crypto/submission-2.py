class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        lowest = prices[0]
        for num in prices:
            maxP = max(maxP, num - lowest)
            lowest = min(num, lowest)
        return maxP

      



        
        