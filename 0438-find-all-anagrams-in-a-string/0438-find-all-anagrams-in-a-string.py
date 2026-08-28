class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_dict = {}
        ans = []
        window = {}
        for ch in p:
            if ch in p_dict:
                p_dict[ch] += 1
            else:
                p_dict[ch] = 1
        k = len(p)
        for i in range(len(s)):
            ch = s[i]
            if ch in window:
                window[ch] += 1
            else:
                window[ch] = 1

            if i >= k:

                old = s[i-k]
                window[old] -= 1

                if window[old] == 0:
                    del window[old]
            if window == p_dict:
                ans.append(i-k+1)
        return ans