class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        isoMap = {}
        for i in range(len(s)):
            if (s[i] in isoMap) and (isoMap[s[i]] == t[i]):
                continue
            elif (s[i] in isoMap) and (isoMap[s[i]] != t[i]):
                return False
            elif (s[i] not in isoMap) and (t[i] in isoMap.values()):
                return False
            else:
                isoMap[s[i]] = t[i]
        return True


s = Solution()
print(s.isIsomorphic("egg", "add"))
print(s.isIsomorphic("foo", "bar"))
print(s.isIsomorphic("paper", "title"))
