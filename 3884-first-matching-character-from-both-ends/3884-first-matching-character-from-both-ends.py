class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n = len(s)
        s = list(s)
        for i in range(n):
            if s[i] == s[n-i-1]:
                flag = True
                return i
            else:
                flag = False
        if flag == False:
            return -1