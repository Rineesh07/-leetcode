class Solution:
    def reverseDegree(self, s: str) -> int:
        alpha ='abcdefghijklmnopqrstuvwxyz'
        values = []
        d = {}
        i = 26
        while i >= 0 :
            values.append(i)
            i -= 1
        for i in range(26):
            d[alpha[i]] = values[i]
        print(d)
        ans = 0
        for i in range(0,len(s)):
            for k , v  in d.items():
                if s[i] == k:
                    ans += v * (i + 1 )
        return ans
