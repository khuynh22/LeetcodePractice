from functools import reduce
import textwrap


class Solution:
    def findSubstring(self, s: str, words):
        word_length = len(words[0])
        total_words_length = word_length * len(words)
        result_indexes = []
        memo = []
        for i in range(len(s)):
            search = s[i:total_words_length+i]

            if len(search) == total_words_length:
                if search in memo:
                    result_indexes.append(i)
                else:
                    _words = sorted(words)
                    _test_words = sorted(textwrap.wrap(search, word_length))

                    if _words == _test_words:
                        memo.append(search)
                        result_indexes.append(i)

        return result_indexes


s = Solution()
print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))
print(s.findSubstring("wordgoodgoodgoodbestword",
      ["word", "good", "best", "word"]))
print(s.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))
print(s.findSubstring("foobarfoobar", ["foo", "bar"]))
