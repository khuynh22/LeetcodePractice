class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if needle == haystack[i:i + len(needle)]:
                return i

        return -1


s = Solution()
print(s.strStr("sadbutsad", "sad"))
print(s.strStr("leetcode", "leeto"))
print(s.strStr("a", "a"))
