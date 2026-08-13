class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        i = 0 
        cnt = 0
        max_len = 1 
        for i in range(len(nums)):
            if nums[i] > nums[i - 1]:
                cnt += 1
                max_len = max(cnt,max_len)
                i += 1
            else:
                cnt = 1
                i += 1
        return max_len