class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sPoint, tPoint = 0, 0
        while sPoint < len(s) and tPoint < len(t):
            if s[sPoint] == t[tPoint]:
                sPoint += 1
                tPoint += 1
            else:
                tPoint += 1
        return sPoint == len(s)


s = Solution()
print(s.isSubsequence("abc", "ahbgdc"))
print(s.isSubsequence("axc", "ahbgdc"))
