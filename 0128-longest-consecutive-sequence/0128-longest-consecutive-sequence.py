class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        print(n)
        if n == 0 :
            return 0
        if n == 1:
            return 1
        nums.sort()
        cnt = 1
        max_cnt = 1 
        i = 0 
        j = i + 1
        while j < len(nums):
            if nums[j] == nums[i] + 1:
                cnt += 1
                max_cnt = max(cnt,max_cnt)
            elif nums[i] == nums[j]:
                pass
            else:
                cnt = 1
            i += 1
            j += 1
        return max_cnt