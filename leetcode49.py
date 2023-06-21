class Solution:
    def groupAnagrams(self, strs):
        wordMap = {}
        for s in strs:
            sortWord = ''.join(sorted(s))
            if sortWord in wordMap.keys():
                wordMap[sortWord].append(s)
            else:
                wordMap[sortWord] = [s]
        
        res = []
        for w in wordMap:
            res.append(wordMap[w])

        return res
    
s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["a"]))