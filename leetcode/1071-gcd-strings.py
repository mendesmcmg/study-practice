class Solution:
  def gcdOfStrings(self, str1: str, str2: str) -> str:
    len1 = len(str1)
    len2 = len(str2)
    minlen = min(len1,len2)
    maxlen = max(len1,len2)
    base = str2 if len1 > len2 else str1
    minim = base
    other = str1 if len1 > len2 else str2
    for i in range(minlen, -1, -1):
      lenb = len(base)
      if base == "":
        return base
      elif maxlen % lenb == 0 and minlen % lenb == 0 and base * int(maxlen/lenb) == other and base * int(minlen/lenb) == minim:
        return base
      else:
        base = base[:-1]

