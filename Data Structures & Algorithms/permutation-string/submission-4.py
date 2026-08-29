class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counted = defaultdict(int)
        for s in s1:
            s1_counted[s] += 1
        s1_n = len(s1)
        # check if the current str is in the s1 list
        left = 0
        s2_counted = defaultdict(int)
        for i in range(len(s2)):
            window = s2[i:i+s1_n]
            s2_counted = defaultdict(int)
            for s in window:
                s2_counted[s] += 1
            if s1_counted == s2_counted:
                return True
        return False
