class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for a, b in points:
            dist = a ** 2 + b ** 2
            minHeap.append([dist, a, b])
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, a, b = heapq.heappop(minHeap)
            res.append([a, b])
            k -= 1
        return res


        