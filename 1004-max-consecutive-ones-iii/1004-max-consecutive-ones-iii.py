class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        cnt = 0
        max_cnt = 0 
        left = 0 
        for right in range(len(nums)):
            if nums[right] == 0 :
                cnt += 1
            while cnt > k:
                if nums[left] == 0 :
                    cnt -= 1
                left += 1
            max_cnt = max(max_cnt,right - left + 1)
        return max_cnt
            