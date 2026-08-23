class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        d = {}
        ans = []
        for i in bulbs :
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for k , v in d.items():
            if v % 2 != 0 :
                ans.append(k)
        ans.sort()
        return ans