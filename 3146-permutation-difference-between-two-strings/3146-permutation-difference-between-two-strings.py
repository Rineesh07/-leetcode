class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        i = 0 
        sd = {}
        td = {}
        for x in s:
            sd[x] = i
            i += 1
        i = 0
        for x in t:
            td[x] = i
            i += 1
        print(sd,td)
        diff = 0
        for key , val in sd.items():
            for k , v in td.items():
                if key == k:
                    diff += abs(sd[key] - td[key])
        return diff
