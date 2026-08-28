class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        missing = 1
        for n in nums:
            if n == missing :
               missing += 1
            elif n > missing:
                break
        return missing