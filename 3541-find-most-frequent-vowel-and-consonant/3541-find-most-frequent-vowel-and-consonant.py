class Solution:
    def maxFreqSum(self, s: str) -> int:
        max_vo = 0
        max_con = 0 
        vowles = {'a' , 'e' , 'i' , 'o' , 'u'}
        d = {}
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        for key , value  in d.items():
            if key in vowles:
                max_vo = max(max_vo,value)
            else:
                max_con = max(max_con,value)
        return max_vo + max_con

        