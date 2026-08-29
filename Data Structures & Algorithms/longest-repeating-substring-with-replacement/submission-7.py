class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        l = 0
        max_substr = 0
        mf = 0
        
        for i, r in enumerate(s):
            counter[r] += 1
            mf = max(mf, counter[r])  # Running max frequency is more efficient
            
            # Current window length is (i - l + 1)
            while (i - l + 1) - mf > k:
                counter[s[l]] -= 1
                l += 1
                
            max_substr = max(max_substr, i - l + 1)
            
        return max_substr