class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        cur = 0
        sign = 1
        stack = []
        for c in s:
            if c.isdigit():
                cur = cur * 10 +int(c)
            elif c in "+-":
                res += cur * sign
                cur = 0
                if c == "-":
                    sign = -1
                else:
                    sign = 1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res += (cur * sign)
                res *= (stack.pop())
                res += stack.pop()
                cur = 0
            else: 
                continue
        
        res += (cur * sign)
        return res
    
s = Solution()
print(s.calculate("1 + 1"))
print(s.calculate(" 2-1 + 2 "))
print(s.calculate("(1+(4+5+2)-3)+(6+8)"))