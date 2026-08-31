class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        nums = set(nums)
        nums = list(nums)
        n = len(nums)
        if n < 3 :
            return max(nums)
        m = max(nums)
        for i in range(n):
            if nums[i] == m:
                third = nums[i - 2]
        return third
            

            