class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for s in strs:
            lst = [0] * 26
            for i in s:
                lst[ord(i) - ord('a')] += 1
            hmap[tuple(lst)].append(s)
        return list(hmap.values())
            

        
    
            





        
       
            
       



        

        