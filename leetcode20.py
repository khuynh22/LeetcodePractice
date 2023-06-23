class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in "[{(":
                stack.append(s[i])
            elif s[i] == ")":
                if len(stack) != 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif s[i] == "]":
                if len(stack) != 0 and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif s[i] == "}":
                if len(stack) != 0 and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False
    
s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))