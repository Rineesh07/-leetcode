def isvowel(s):
    v = 'aeiou'
    for ch in s:
        if ch in v:
            return True
        else:
            return False
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_cnt = 0 
        cnt = 0
        for i in range(k):
            if isvowel(s[i]):
                cnt +=1
        max_cnt = cnt
        for i in range(k,len(s)):
            if isvowel(s[i]):
                cnt += 1
            if isvowel(s[i-k]):
                cnt -= 1
            max_cnt = max(cnt,max_cnt)
        return max_cnt

       
            
        