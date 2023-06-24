class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        banks = {}
        notes = {}
        for w in magazine:
            banks[w] = 1 + banks.get(w, 0)

        for w in ransomNote:
            notes[w] = 1 + notes.get(w, 0)

        for w in notes:
            if not (w in banks.keys() and notes[w] <= banks[w]):
                return False
        return True


s = Solution()
print(s.canConstruct("a", "b"))
print(s.canConstruct("aa", "ab"))
print(s.canConstruct("aa", "aab"))
