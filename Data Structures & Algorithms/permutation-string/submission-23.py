from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counted = Counter(s1)
        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len > s2_len: 
            return False
        left = 0 
        window = s2[left:s1_len]
        window_counted = Counter(window)
        if window_counted == s1_counted:
            return True
        for right in range(s1_len, s2_len):
            window_counted[s2[right]] += 1
            window_counted[s2[right-s1_len]] -= 1
            if window_counted[s2[right-s1_len]] == 0:
                del window_counted[s2[right-s1_len]]
            if window_counted == s1_counted:
                return True
        
        return False

