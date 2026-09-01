class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Montonic Decreasing Stack
        results = [0] * len(temperatures)
        pending = []
        n_temp = len(temperatures)
        for i in range(n_temp):
            while pending and temperatures[pending[-1]] < temperatures[i]:
                prev_idx = pending[-1]
                diff_idx = i - prev_idx
                results[prev_idx] = diff_idx
                pending.pop()
            # pending_res = [temperatures[i] for i in pending]
            # print(f"pending state: {pending_res}")
            pending.append(i)
        return results
        
