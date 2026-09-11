class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for x in s:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        first_ch = '@'
        for k , v in d.items():
            if v == 1:
                first_ch = k
                break
        print(first_ch)
        n = len(s)
        for i in range(n):
            if s[i] == first_ch:
                return i
        return -1