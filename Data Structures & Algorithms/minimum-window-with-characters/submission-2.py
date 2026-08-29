from collections import Counter
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n_s, n_t = len(s), len(t)
        if n_s < n_t:
            return ""
        if not set(t).issubset(set(s)):
            return ""
            
        t_count = Counter(t) # how many of each character t needs
        required = len(t_count) # how many DISTINCT characters must be satisfied
        
        l = 0
        min_size = float('inf')
        min_window = ""
        
        # look for indices
        inc_indices = [i for i in range(n_s) if s[i] in t_count]
        
        window_counts = defaultdict(int)
        formed = 0 # the number of DISTINCT characters have been satisfied
        
        # Replace the nested loops with a two-pointer sliding window over inc_indices
        for r in range(len(inc_indices)):
            right_idx = inc_indices[r]
            char = s[right_idx]
            window_counts[char] += 1
            
            # Why do we need char in t_count check? 
            # Rules to be considered Formed.
                # 1. the character exist in DISTINCT character in t
                # 2. the window counts matches the t count for that character
            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1
            
            # This stage is when all the characters are in place. 
            while l <= r and formed == required:
                left_idx = inc_indices[l]
                curr_len = right_idx - left_idx + 1
                
                # Update if the smallest
                if curr_len < min_size:
                    min_size = curr_len
                    min_window = s[left_idx:right_idx + 1]
                    
                left_char = s[left_idx]
                window_counts[left_char] -= 1
                
                #
                if left_char in t_count and window_counts[left_char] < t_count[left_char]:
                    formed -= 1
                l += 1
                
        return min_window