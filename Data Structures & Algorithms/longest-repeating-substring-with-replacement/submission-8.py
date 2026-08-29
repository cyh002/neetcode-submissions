from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        n = len(s)
        l = 0
        substr = []
        max_substr = 0
        mf = 0
        for i, r in enumerate(s):
            # print(f"Loop {i}, r : {r}")
            counter[r] += 1
            mf = max(mf, counter[r])
            substr.append(r)
            # print(f"Append. Substr: {substr}")
            while (i - l + 1) - mf > k:
                counter[s[l]] -= 1
                l += 1
            max_substr = max(max_substr, i - l + 1)
        return max_substr
        






                


