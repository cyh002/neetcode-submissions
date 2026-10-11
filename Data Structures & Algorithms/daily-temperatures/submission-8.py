class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic decreasing, hunting bigger
        stack = []
        n_temps = len(temperatures)
        results = [0] * n_temps
        
        # constantly pop if the stacks elements are smaller than the temp in temperatures
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                results[idx] = i - idx
            stack.append(i)
        return results