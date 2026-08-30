from collections import Counter
from collections import defaultdict

# pseudo code:
# window valid if
    # 1. all the char exist in t
    # 2. gotten = need

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not set(t).issubset(set(s)):
            return ""
        n_s , n_t = len(s) , len(t)
        s_set, t_set = set(s), set(t)
        result_indices = [-1, -1]
        t_counted = Counter(t)
        need = len(t_counted)
        gotten = 0
        s_counted = defaultdict(int)
        l = 0
        min_len = float("inf")
        for r in range(n_s):
            c = s[r]
            if c in t_set:
                s_counted[c] += 1
                if s_counted[c] == t_counted[c]:
                    gotten += 1
        
                # if the window is valid, contains all. 
                while gotten == need and r >= l:
                    if min_len >= (r - l + 1):
                        # update the result
                        min_len = (r - l + 1)
                        result_indices = [l,r]
                    if s[l] in t_set:
                        s_counted[s[l]] -= 1
                        if s_counted[s[l]] == t_counted[s[l]] - 1:
                            gotten -= 1
                    l += 1
        return s[result_indices[0]:result_indices[1]+1]
                        




        
        