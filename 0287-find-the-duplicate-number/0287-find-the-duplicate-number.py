class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        i = 0 
        j = i + 1
        while j <= len(nums)-1:
            if nums[i] != nums[j]:
                i += 1
                j += 1
            else:
                return nums[i]