class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        last = len(s) - 1
        while s[last] == " ":
            last -= 1

        for i in range(last, -1, -1):
            if s[i] != " ":
                res += 1
            else:
                break

        return res


s = Solution()
print(s.lengthOfLastWord("Hello World"))
print(s.lengthOfLastWord("   fly me   to   the moon  "))
print(s.lengthOfLastWord("luffy is still joyboy"))
