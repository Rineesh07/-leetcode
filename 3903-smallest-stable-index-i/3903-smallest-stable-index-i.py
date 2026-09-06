class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        scores = []
        n = len(nums)
        i = 0 
        for i in range(n):
            left_max = max(nums[0:i+1])
            right_min = min(nums[i:])
            s = left_max - right_min
            scores.append(s)
        print(scores)
        for i in range(n):
            if scores[i] <= k:
                return i
        return -1