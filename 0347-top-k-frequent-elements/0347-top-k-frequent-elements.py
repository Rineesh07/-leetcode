class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        ans = []
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        d = dict(sorted(d.items(), key = lambda item : item[1] , reverse = True))
        ans = [key for key , value in d.items()]
        return ans[:k]
        