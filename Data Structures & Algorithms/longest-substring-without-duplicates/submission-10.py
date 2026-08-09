class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = defaultdict()
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in char:
                l = max(char[s[r]] + 1, l)
            char[s[r]] = r
            res = max(res, r - l + 1)
        return res

            
        
            

        