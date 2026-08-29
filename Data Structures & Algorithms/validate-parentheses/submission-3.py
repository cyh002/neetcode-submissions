class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parent_dict = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        n = len(s)
        for i in range(n):
            current = s[i]
            if current in parent_dict:
                if stack and parent_dict[current] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(current)
        return False if stack else True