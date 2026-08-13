class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnt = {}  
        for i in s:
            if i in cnt.keys():
                cnt[i] += 1
            else:
                cnt[i] = 1
        for j in t:
            if j in cnt.keys():
                cnt[j] -= 1
            else:
                cnt[j] = 1
        for k in cnt:
            if cnt.get(k) != 0:
                return False 
        return True   
        