class Solution(object):
    def numIdenticalPairs(self, nums):
        cnt = 0 
        d = {}
        for n in nums:
            if n in d:
                cnt += d[n]
                d[n] += 1
            else:
                d[n] = 1
        return cnt
        