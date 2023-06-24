class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        res = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "I":
                if i + 1 < len(s) and s[i + 1] in "VX":
                    res -= 1
                else:
                    res += 1
            elif s[i] == "X":
                if i + 1 < len(s) and s[i + 1] in "LC":
                    res -= 10
                else:
                    res += 10
            elif s[i] == "C":
                if i + 1 < len(s) and s[i + 1] in "DM":
                    res -= 100
                else:
                    res += 100
            elif s[i] == "V":
                res += 5
            elif s[i] == "L":
                res += 50
            elif s[i] == "D":
                res += 500
            else:
                res += 1000
        return res
