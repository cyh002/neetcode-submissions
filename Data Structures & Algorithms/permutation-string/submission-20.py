from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Brute Force
        # s1_n, s2_n = len(s1), len(s2)
        # for i in range(s2_n):
        #     # check
        #     if Counter(s2[i:i+s1_n]) == Counter(s1):
        #         return True
        # return False
        # sliding window
        s1_n, s2_n = len(s1), len(s2)
        subject = Counter(s1)
        if subject == Counter(s2):
            return True
        window_count = Counter(s2[:s1_n])
        if window_count == subject:
            return True
        for i in range(s1_n, s2_n):
            # add to the right
            window_count[s2[i]] += 1
            # remove to the left
            left_i = i - s1_n
            window_count[s2[left_i]] -= 1
            if window_count[s2[left_i]] == 0:
                del window_count[s2[left_i]]
            if window_count == subject:
                return True
        return False
        