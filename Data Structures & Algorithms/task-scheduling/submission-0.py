from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-c for c in Counter(tasks).values()]  # names don't matter, only counts
        heapq.heapify(heap)
        cooling = deque()  # (neg_count, time_it_can_return)
        time = 0

        while heap or cooling:
            time += 1
            if heap:
                cnt = heapq.heappop(heap) + 1
                if cnt < 0:
                    cooling.append((cnt, time + n))
            # else: idle tick, nothing runs

            if cooling and cooling[0][1] == time:
                heapq.heappush(heap, cooling.popleft()[0])
        return time