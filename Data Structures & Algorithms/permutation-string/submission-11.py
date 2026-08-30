from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)
        l = 0
        counted_s1 = Counter(s1)
        for i in range(len_s2):
            if Counter(s2[i:i+len_s1]) == counted_s1:
                return True
        return False