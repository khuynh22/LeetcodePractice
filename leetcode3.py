class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        res = 0
        l = 0
        checkStr = ""
        for r in range(len(s)):
            if s[r] not in checkStr:
                checkStr += s[r]
                res = max(res, r - l + 1)
            else:
                res = max(res, r - l)
                while (s[r] in checkStr):
                    checkStr = checkStr[1:]
                    l += 1
                checkStr += s[r]
                res = max(res, r - l)

            print(checkStr)
        return res
