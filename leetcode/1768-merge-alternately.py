class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        rangemax = max(len1, len2)
        rangemin1 = 0 if len1 > len2 else 1
        out = ""
        for i in range(rangemax):
            if rangemin1 == 1 and i < len1:
                out+= word1[i]
                out+=word2[i]
                continue
            if rangemin1 == 0 and i < len2:
                out+= word1[i]
                out+=word2[i]
                continue
            elif rangemin1 == 1:
                out+=word2[i]
            elif rangemin1 == 0:
                out+= word1[i]
        return out
        