class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pairs_sum = []
        print(nums)
        left = 0
        n = len(nums)
        right = n - 1
        while left < right :
            pairs_sum.append((nums[left]+nums[right]))
            left += 1
            right -=1
        print(pairs_sum)
        return max(pairs_sum)
