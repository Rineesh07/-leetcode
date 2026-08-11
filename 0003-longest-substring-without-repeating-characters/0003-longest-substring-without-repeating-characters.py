class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_cnt = 0
        t = set()
        for right in range(len(s)):
            while s[right] in t:
                t.remove(s[left])
                left += 1
            t.add(s[right])
            max_cnt = max(max_cnt,right-left+1)
        return max_cnt