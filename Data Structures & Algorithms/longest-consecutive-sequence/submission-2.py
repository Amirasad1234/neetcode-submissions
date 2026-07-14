class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        count = 0
        for n in numSet:
            if (n - 1) not in numSet:
                j = n
                count = 0
                while j in numSet:
                    j += 1
                    count += 1
                res = max(count, res)
        return res


           

                

            


       

            

   
        