class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d = {}
        ans = []
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        for k , v in d.items():
            if v == 2 :
                ans.append(k)
        return ans

        