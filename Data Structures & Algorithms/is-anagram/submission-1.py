from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. split the first text into list and second into list too
        # 2. count the number of letters 
        # 3. compare the number 
        s_count = Counter(s)
        t_count = Counter(t)
        return s_count == t_count
        