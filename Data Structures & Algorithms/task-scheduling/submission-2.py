from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. How do we know which task to prioritize?
            # A: Prioritise the task with the most count. 
        # 2. How do we manage the cooldown?
            # B: track the current time + n. then once the cooldown finishes, add it back to the heap queue
        
        # Only the values of the task_count matter for counting. 
        countMaxHeap = [(-c, t) for t, c in Counter(tasks).items()] # [(2,X), (2,Y)]
        heapq.heapify(countMaxHeap)
        # we choose deque cause we trying to popleft
        cooling = deque() # append ((-count, name), cooldown)
        order = []
        time = 0
        while countMaxHeap or cooling:
            time += 1
            if countMaxHeap:
                neg_cnt, name = heapq.heappop(countMaxHeap)
                remaining = -neg_cnt - 1
                # if the task is not done
                if remaining > 0:
                    cooldown = time + n
                    cooling.append(((-remaining, name), cooldown))
                order.append(name)
            else:
                order.append("idle")
            # if there are any cooling task that is equal to the time
            if cooling and cooling[0][1] == time:
                task_in = cooling.popleft()[0]
                heapq.heappush(countMaxHeap, task_in)
        return len(order)




        

        