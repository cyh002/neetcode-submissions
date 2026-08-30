from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)
        counted_s1 = Counter(s1)
        window = s2[:len_s1]
        counted_window = Counter(window)
        if counted_window == counted_s1:
            return True
        for r in range(len_s1, len_s2): # len_s1 = 2, len_s2 = 8
            counted_window[s2[r]] += 1
            counted_window[s2[r - len_s1]] -= 1 # 5 - 2 - 1 = 3
            if counted_window == counted_s1:
                return True
        return False
        