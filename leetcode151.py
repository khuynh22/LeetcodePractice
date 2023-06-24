class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        res = ""
        for i in range(len(words) - 1, 0, -1):
            res += words[i] + " "

        res += words[0]
        return res


s = Solution()
print(s.reverseWords("the sky is blue"))
print(s.reverseWords("  hello world  "))
print(s.reverseWords("a good   example"))
