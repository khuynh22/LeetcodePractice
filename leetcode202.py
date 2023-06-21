class Solution:
    def isHappy(self, n: int) -> bool:
        arr = []
        while n != 1:
            if n in arr:
                return False
            arr.append(n)
            numList = [int(i) for i in str(n)]
            n = sum(i**2 for i in numList)
        return True

s = Solution()
print(s.isHappy(19))
print(s.isHappy(2))