class Solution:
  def gcdOfStrings(self, str1: str, str2: str) -> str:
    len1 = len(str1)
    len2 = len(str2)
    base = str2
    for i in range(len2, -1, -1):
      lenb = len(base)
      if base == "" or len1 % lenb == 0 and base * int(len1/lenb) == str1:
        return base
      else:
        base = base[:-1]
