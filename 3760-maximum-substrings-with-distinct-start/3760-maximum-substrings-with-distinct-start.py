class Solution:
    def maxDistinct(self, s: str) -> int:
        substr = set(s)
        return len(substr)