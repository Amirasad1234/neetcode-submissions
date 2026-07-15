class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        l = 0
        hset = set()
        for r, s1 in enumerate(s):
            while s1 in hset:
                hset.remove(s[l])
                l += 1
            hset.add(s1)
            count = max(count, r - l + 1)
        return count
            



      