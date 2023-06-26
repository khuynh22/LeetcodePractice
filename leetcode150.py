class Solution:
    def evalRPN(self, tokens) -> int:
        numStack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                first = numStack.pop()
                second = numStack.pop()
                numStack.append(first + second)
            elif tokens[i] == "-":
                first = numStack.pop()
                second = numStack.pop()
                numStack.append(second - first)
            elif tokens[i] == "*":
                first = numStack.pop()
                second = numStack.pop()
                numStack.append(first * second)
            elif tokens[i] == "/":
                first = numStack.pop()
                second = numStack.pop()
                numStack.append(int(float(second) / first))
            else:
                numStack.append(int(tokens[i]))
        return numStack.pop()
