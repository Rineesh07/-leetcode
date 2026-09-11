class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i = 0 
        n = len(nums)
        nums.sort()
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        print(d)
        for k , v in d.items():
            if v == 1:
                return k