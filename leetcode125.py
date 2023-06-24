class Solution:
    def isPalindrome(self, s: str) -> bool:
        convert = ""
        for i in range(len(s)):
            if s[i].isalnum():
                convert += s[i].lower()

        return convert == convert[::-1]


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome(" "))
