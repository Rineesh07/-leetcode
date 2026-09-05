class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        print(d)
        l = []
        for key,value in d.items():
            if value > len(nums) // 3:
                l.append(key)
        return l