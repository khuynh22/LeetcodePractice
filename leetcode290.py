class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sArr = s.split(' ')
        if len(pattern) != len(sArr):
            return False
        wordMap = {}
        for i in range(len(pattern)):
            if pattern[i] in wordMap and wordMap[pattern[i]] == sArr[i]:
                continue
            elif pattern[i] in wordMap and wordMap[pattern[i]] != sArr[i]:
                return False
            elif pattern[i] not in wordMap and sArr[i] in wordMap.values():
                return False
            else:
                wordMap[pattern[i]] = sArr[i]
        return True

s = Solution()
print(s.wordPattern("abba", "dog cat cat dog"))
print(s.wordPattern("abba", "dog cat cat fish"))
print(s.wordPattern("aaaa", "dog cat cat dog"))
print(s.wordPattern("aaa", "aa aa aa aa"))