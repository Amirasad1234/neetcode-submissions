class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        res, resLen = [-1, 1], float('inf')
        l = 0
        CountT = {}
        window = {}
        for c in t:
            CountT[c] = 1 + CountT.get(c, 0)
        have, need = 0, len(CountT)

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in CountT and window[c] == CountT[c]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in CountT and window[s[l]] < CountT[s[l]]:
                    have -=1
                l += 1
        l, r = res
        return s[l:r + 1] if resLen != float('inf') else ''


        

                



        

        