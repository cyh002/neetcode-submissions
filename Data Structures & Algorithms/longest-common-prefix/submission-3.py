class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # split
        first = strs[0]
        # for each char
        for i in range(len(first)):
            char = first[i]
            for other in strs[1:]:
                if i == len(other) or char != other[i]:
                    return first[:i]
        return first
