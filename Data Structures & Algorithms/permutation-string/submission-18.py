from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Brute Force
        s1_n, s2_n = len(s1), len(s2)
        for i in range(s2_n):
            # check
            if Counter(s2[i:i+s1_n]) == Counter(s1):
                return True
        return False