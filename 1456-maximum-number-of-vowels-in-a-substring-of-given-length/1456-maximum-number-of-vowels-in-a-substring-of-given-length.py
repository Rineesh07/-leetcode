def isvowel(ch) -> bool :
    v = 'aeiou'
    if ch not in v:
        return False
    else:
        return True
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cnt = 0 
        max_cnt = 0  
        for i in range(k):
            if isvowel(s[i]):
                cnt += 1
                max_cnt = max(cnt,max_cnt)
        for i in range(k,len(s)):
            if isvowel(s[i]) :
                cnt += 1
            if isvowel(s[i-k]):
                cnt -= 1 
            max_cnt = max(max_cnt,cnt)
        return max_cnt
        
            
        
        