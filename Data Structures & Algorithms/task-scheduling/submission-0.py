class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        mHeap = [-cnt for cnt in count.values()]
        heapq.heapify(mHeap)

        time = 0
        q = deque()

        while mHeap or q:
            time += 1

            if mHeap:
                cnt = 1 + heapq.heappop(mHeap)
                if cnt:
                    q.append([cnt, time + n])
                
            if q and q[0][1] == time:
                heapq.heappush(mHeap, q.popleft()[0])    
        return time
               






        