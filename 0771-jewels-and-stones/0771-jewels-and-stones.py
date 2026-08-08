class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        for j in jewels:
            for s in stones:
                if j == s:
                    cnt += 1
        return cnt
        