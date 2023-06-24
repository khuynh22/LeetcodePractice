class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        mapOfRow, numberOfRow = {}, 0
        j = 0
        strKeep = 0
        while j < len(words):
            if strKeep == 0:
                strKeep += len(words[j])
                mapOfRow[numberOfRow] = [words[j]]
            elif strKeep + len(words[j]) + 1 <= maxWidth:
                strKeep += 1 + len(words[j])
                mapOfRow[numberOfRow].append(words[j])
            else:
                strKeep = 0
                numberOfRow += 1
                j -= 1
            j += 1

        for words in list(mapOfRow.values())[:len(mapOfRow) - 1]:
            strAdd = ""
            rem = maxWidth - sum(len(words[i]) for i in range(len(words)))
            for i in range(len(words) - 1):
                words[i] += (rem // (len(words) - 1) * " ")
                if i < rem % (len(words) - 1):
                    words[i] += " "
                strAdd += words[i]
            if len(words) > 1:
                strAdd += words[-1]
            else:
                strAdd += words[-1] + rem * " "
            res.append(strAdd)

        strAddLast = ""
        lastValue = list(mapOfRow.values())[-1]
        for i in range(len(lastValue) - 1):
            strAddLast += lastValue[i] + " "

        print(strAddLast)
        strAddLast += lastValue[-1] + (" " * (maxWidth - sum(len(lastValue[i])
                                       for i in range(len(lastValue))) - len(lastValue) + 1))
        # res.pop()
        res.append(strAddLast)

        return res
