class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 1:
            return strs[0]
        
        res = ""
        strs.sort()
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                res += strs[0][i]
            else:
                break
        
        return res

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))