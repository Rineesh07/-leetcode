class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        length =  0
        for ch in s :
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        print(d)
        found = False
        for v in d.values():
            if v % 2 == 0 :
                length += v
            else:
                length += v - 1
                found = True
        print(length)
        if found :
            return length + 1
        else:
            return length
        