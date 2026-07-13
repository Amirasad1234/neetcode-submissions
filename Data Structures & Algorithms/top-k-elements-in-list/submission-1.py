class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        res = []
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for val, freq in count.items():
            minHeap.append([-freq, val])
        heapq.heapify(minHeap)
        for _ in range(k):
            freq, val = heapq.heappop(minHeap)
            res.append(val)
        return res
            


        


       
            
        
      

        








        