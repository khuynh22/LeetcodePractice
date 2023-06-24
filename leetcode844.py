class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        p1 = 0
        p2 = 0
        while p1 < len(s) and p2 < len(t):
            if s[p1] != '#':
                stack1.append(s[p1])
            else:
                if len(stack1) > 0:
                    stack1.pop()

            if t[p2] != '#':
                stack2.append(t[p2])
            else:
                if len(stack2) > 0:
                    stack2.pop()

            p1 += 1
            p2 += 1

        if p1 < len(s):
            while p1 < len(s):
                if s[p1] != '#':
                    stack1.append(s[p1])
                else:
                    if len(stack1) > 0:
                        stack1.pop()
                p1 += 1

        elif p2 < len(t):
            while p2 < len(t):
                if t[p2] != '#':
                    stack2.append(t[p2])
                else:
                    if len(stack2) > 0:
                        stack2.pop()
                p2 += 1

        return stack1 == stack2


s = Solution()
print(s.backspaceCompare("ab#c", "ad#c"))
print(s.backspaceCompare("ab##", "c#d#"))
print(s.backspaceCompare("a#c", "b"))
